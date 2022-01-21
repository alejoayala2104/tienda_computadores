"""AUTOR: Andrés Alejandro Ayala Chamorro
"""

from tienda_gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

from computador import Computador
from ed.jerarquicas.arbolBinarioBusqueda import ArbolBinarioBusqueda
from ed.jerarquicas.recorridos import cad_inorden,cad_postorden

class Ventana(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Se crea el arbol binario de búsqueda
        self.arbol = ArbolBinarioBusqueda()

        self.ganancias = 0.0
        self.ui.txfGanancias.setText(str(self.ganancias))

        #Asignando funcionalidad
        self.ui.btnGuardar.clicked.connect(self.anadirComputador)
        self.ui.btnVender.clicked.connect(self.venderComputador)
        self.ui.btnGenerar.clicked.connect(self.generarReporte)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnSalir.clicked.connect(self.close)

        #Asignando estilos
        self.ui.btnGuardar.setObjectName("botonMain")
        self.ui.btnVender.setObjectName("botonMain")
        self.ui.btnGenerar.setObjectName("botonMain")
        self.ui.btnLimpiar.setObjectName("botonMain")
        self.ui.btnSalir.setObjectName("botonMain")

    def anadirComputador(self):
        marca = self.ui.txfAnadirMarca.text()
        vel = self.ui.txfAnadirVel.text()
        precio = self.ui.txfAnadirPrecio.text()

        #Validación de campos vacíos
        if marca and vel and precio:
            #Validación precio numérico           
            if precio.isnumeric():
                #Validar que el computador exista
                computador = self.arbol.buscar(Computador(marca, vel, precio))
                if computador:
                    # Si lo encontró, muestre el mensaje de que ya existe
                    # Esto se hace solamente para mostrar el mensaje porque el método adicionar
                    # de árbol binario de búsqueda no lo añadirá.
                    QtWidgets.QMessageBox.critical(self,
                        'Computador existente','El computador ya existe en el inventario.')                          
                else:                    
                    self.arbol.adicionar(Computador(marca,vel,float(precio)))#Nuevo computador añadido al árbol

                    #Se actualiza el reporte 
                    self.generarReporte()

                    #Se limpian las casillas
                    self.ui.txfAnadirMarca.clear()        
                    self.ui.txfAnadirVel.clear()        
                    self.ui.txfAnadirPrecio.clear()                                     
            else:
                QtWidgets.QMessageBox.critical(self,
                'Precio inválido','El precio debe ser un valor numérico.')                
        else:
            QtWidgets.QMessageBox.critical(self,
                'Error','Por favor complete todos los campos.')

    def venderComputador(self):
        marca = self.ui.txfVenderMarca.text()
        vel = self.ui.txfVenderVel.text()
        computador = self.arbol.buscar(Computador(marca,vel,0.0))        
        if computador:#Si se encontró el computador -> Venderlo (borrarlo)
            ganancia = computador.precio * 0.15
            pVenta = computador.precio + ganancia
            self.ui.txfVenderPrecio.setText('$ ' + str(pVenta))#Se muestra el precio de venta
            #Confirmación de venta
            msgVenta = 'Se venderá el computador:\n' + str(computador) + '\nPrecio de venta de $' + str(pVenta)                
            respVenta = QtWidgets.QMessageBox.question(self,
            'Confirmar venta',msgVenta + '\n¿Desea confirmar la venta?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            #Si se confirma la venta
            if respVenta == QtWidgets.QMessageBox.Yes:
                self.arbol.borrar(computador)
                QtWidgets.QMessageBox.information(self,
                    'Venta exitosa','El computador fue vendido con éxito.')

                #Se actualizan las ganancias                
                self.ganancias += ganancia
                self.ui.txfGanancias.setText(str(self.ganancias))

                #Se actualiza el reporte 
                self.generarReporte()

                #Se limpia las casillas
                self.ui.txfVenderMarca.clear()
                self.ui.txfVenderVel.clear()
                self.ui.txfVenderPrecio.setText("$ 0.0")
            else:
                QtWidgets.QMessageBox.critical(self,
                    'Venta cancelada','La venta fue cancelada.')
                self.ui.txfVenderPrecio.setText("$ 0.0")
        else:
            QtWidgets.QMessageBox.critical(self,
                'Computador no encontrado','El computador ingresado no existe en inventario.')   
            self.ui.txfVenderPrecio.setText("$ 0.0")         
        
    def generarReporte(self):
        cad = "Reporte de la tienda\n======================"
        cad += "\nComputador mínimo: " + str(self.arbol.buscar_minimo())
        cad += "\nComputador máximo: " + str(self.arbol.buscar_maximo())
        cad += "\nNúmero total de computadores: " + str(len(self.arbol))
        cad += "\n\n==========INVENTARIO=========="
        if self.ui.cbxRecorrido.currentText() == "Inorden":
            cad += cad_inorden(self.arbol)
        else:
            cad += cad_postorden(self.arbol)
        
        self.ui.txaReporte.setText(cad)

    def limpiar(self):
        self.ui.txaReporte.clear()

stylesheet = """
QMainWindow {
    background-color: white;
}

QLabel{
    color: #5B5149;    
}

QPushButton#botonMain{
    background-color: #5B9279;      
    border: 0px;
    color: white;
}

QPushButton#botonMain:hover{
    background-color: #568A73;
}

QPushButton#botonMain:pressed {
    background-color: #4F7D68;    
}

QTextEdit{     
    color: #5B5149;   
    border-width: 1px;
    border-style: solid;
    border-color: #5B9279; 
}

QLineEdit{
    color: #5B5149; 
    border-width: 1px;
    border-style: solid;
    border-color: #5B9279;
}

QComboBox {
    border: 1px solid  #5B9279;
    color: #5B5149; 
}
"""



if __name__ == '__main__':
    app = QtWidgets.QApplication([])    
    widget = Ventana()
    widget.show()
    widget.setStyleSheet(stylesheet)
    app.exec_()