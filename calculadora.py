#===============================================#
# Grupo 2 Integrantes                           #
#       Lucas Barrera Menem                     #
#       Fernando Quintero                       #
#       Gustavo Rios                            #
#===============================================#
import math
from typing import Text
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        self.setWindowTitle("Calculadora")
        #Seteamos los operadores
        self.operador1 = 0
        self.operador2 = 0
        #Seteamos el tipo de operación a realizar
        self.operacion = ""
        #Listeners de Eventos de los botones de los números
        self.boton1.clicked.connect(self.click_1)
        self.boton2.clicked.connect(self.click_2)
        self.boton3.clicked.connect(self.click_3)
        self.boton4.clicked.connect(self.click_4)
        self.boton5.clicked.connect(self.click_5)
        self.boton6.clicked.connect(self.click_6)
        self.boton7.clicked.connect(self.click_7)
        self.boton8.clicked.connect(self.click_8)
        self.boton9.clicked.connect(self.click_9)
        self.boton0.clicked.connect(self.click_0)

        #Listeners de Eventos de los botones de las operaciones
        self.suma.clicked.connect(self.sumar)   
        self.resta.clicked.connect(self.restar)
        self.producto.clicked.connect(self.multiplicar)
        self.division.clicked.connect(self.dividir)
        self.potenciar.clicked.connect(self.potencia)
        self.raizr.clicked.connect(self.raiz)
        self.igual.clicked.connect(self.resultado)

        #Listener de Borrado de termino
        self.borrar_termino.clicked.connect(self.borrar)
        #Listener de borrado de un digito
        self.borrar_undigito.clicked.connect(self.borrar_digito)
        #Listener de Borrado completo
        self.eliminar.clicked.connect(self.borrar_todo)

        #Listener de convertir a negativo
        self.negativo.clicked.connect(self.cambio_signo)

    #Eventos operaciones
    def sumar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "suma"
        else:
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1 + self.operador2))

    def restar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "resta"
        else:
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1 - self.operador2))  

    def multiplicar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "multiplicacion"
        else:
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1 * self.operador2))

    def dividir(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "division"
        else:
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(int(self.operador1/self.operador2)))    

    def potencia(self):
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "potenciar"
        else:
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1**self.operador2))

    def raiz(self):
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "raiz"
            self.Calculo.setText(str(int(math.sqrt(self.operador1))))                          

    def resultado(self):
        #Se procede a la operación dependiendo del tipo y siempre y cuando este determinado el primer operador.
        if(self.operacion == "suma"):
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1+self.operador2))
        elif(self.operacion == "resta"):
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1-self.operador2))
        elif(self.operacion == "multiplicacion"):
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1 * self.operador2))
        elif(self.operacion == "division"):
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(int(self.operador1 / self.operador2)))     
        elif(self.operacion == "potenciar"):
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1**self.operador2))       
        elif(self.operacion == "raiz"):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText(str(math.sqrt(self.operador1)))           

    #Eventos Borrar
    def borrar(self):
        self.Calculo.setText("")

    def borrar_digito(self):
        self.lista_digito = str(self.Calculo.text())
        self.Calculo.setText(self.lista_digito [ : -1 ])

    def borrar_todo(self):  
        self.operador1 = 0
        self.operador2 = 0
        self.Calculo.clear()

    def cambio_signo(self):
        self.Calculo.setText(self.Calculo.text() + "-")    

    #Eventos de asignación de valores al label
    def click_1(self):
        self.Calculo.setText(self.Calculo.text() + "1")

    def click_2(self): 
        self.Calculo.setText(self.Calculo.text() + "2")
    
    def click_3(self): 
        self.Calculo.setText(self.Calculo.text() + "3")
    
    def click_4(self): 
        self.Calculo.setText(self.Calculo.text() + "4")
    
    def click_5(self): 
        self.Calculo.setText(self.Calculo.text() + "5")
    
    def click_6(self): 
        self.Calculo.setText(self.Calculo.text() + "6")
    
    def click_7(self): 
        self.Calculo.setText(self.Calculo.text() + "7")
    
    def click_8(self): 
        self.Calculo.setText(self.Calculo.text() + "8")
    
    def click_9(self): 
        self.Calculo.setText(self.Calculo.text() + "9")
    
    def click_0(self): 
        self.Calculo.setText(self.Calculo.text() + "0")

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()