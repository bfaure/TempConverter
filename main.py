# python 2.7
import os
import sys
import time
import random
from time import sleep

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def fahrenheight2celcius(temp):
	return (temp-32.0)*(5.0/9.0)
def celcius2fahrenheight(temp):
	return temp*(9.0/5.0)+32.0

class MainWindow(QWidget):

	def __init__(self):
		super(MainWindow,self).__init__()
		self.init_vars()
		self.init_ui()

	def init_vars(self):
		self.key_dict={Qt.Key_Left:'left',Qt.Key_Right:'right'}

	def init_ui(self):
		self.main_layout=QVBoxLayout(self)
		horiz_layout=QHBoxLayout()

		self.celcius_label=QLabel("Celcius")

		self.celcius_input=QLineEdit(self)
		#self.celcius_input.setText("0")
		celcius_input_validator=QDoubleValidator()
		self.celcius_input.setValidator(celcius_input_validator)
		self.celcius_input.textEdited.connect(self.celcius_text_changed)

		main_celcius_layout=QVBoxLayout()
		celcius_label_layout=QHBoxLayout()
		celcius_input_layout=QHBoxLayout()

		celcius_input_layout.addWidget(self.celcius_input)
		celcius_label_layout.addWidget(self.celcius_label)

		main_celcius_layout.addStretch(2)
		main_celcius_layout.addLayout(celcius_label_layout)
		main_celcius_layout.addLayout(celcius_input_layout)
		main_celcius_layout.addStretch(2)

		self.fahren_label=QLabel("Fahrenheit")

		self.fahren_input=QLineEdit(self)
		#self.celcius_input.setText("0")
		fahren_input_validator=QDoubleValidator()
		self.fahren_input.setValidator(fahren_input_validator)
		self.fahren_input.textEdited.connect(self.fahren_text_changed)

		main_fahren_layout=QVBoxLayout()
		fahren_label_layout=QHBoxLayout()
		fahren_input_layout=QHBoxLayout()

		fahren_input_layout.addWidget(self.fahren_input)
		fahren_label_layout.addWidget(self.fahren_label)

		main_fahren_layout.addStretch(2)
		main_fahren_layout.addLayout(fahren_label_layout)
		main_fahren_layout.addLayout(fahren_input_layout)
		main_fahren_layout.addStretch(2)

		equals_label=QLabel("=")
		equals_layout=QVBoxLayout()
		equals_layout.addStretch(2)
		equals_layout.addSpacing(10)
		equals_layout.addWidget(equals_label)
		equals_layout.addStretch(2)
 
		horiz_layout.addStretch()
		horiz_layout.addLayout(main_celcius_layout)
		horiz_layout.addLayout(equals_layout)
		horiz_layout.addLayout(main_fahren_layout)
		horiz_layout.addStretch()

		self.main_layout.addLayout(horiz_layout)

		self.connect(QShortcut(QKeySequence(Qt.Key_Escape), self), QtCore.SIGNAL('activated()'), self.quit)

		self.setWindowIcon(QIcon("img/logo.png"))
		self.setWindowTitle("Temperature Converter")
		self.show()

	def quit(self):
		print("\nExiting TempCalc.\n")
		sys.exit(1)

	def fahren_text_changed(self):
		try:
			self.celcius_input.setText(str(fahrenheight2celcius(float(self.fahren_input.text()))))
		except Exception as e:
			self.celcius_input.setText("")
			print(e)

	def celcius_text_changed(self):
		try:
			self.fahren_input.setText(str(celcius2fahrenheight(float(self.celcius_input.text()))))
		except Exception as e:
			self.fahren_input.setText("")
			print(e)


def main():
	pyqt_app = QApplication(sys.argv)
	_ = MainWindow()
	sys.exit(pyqt_app.exec_())

if __name__ == '__main__':
	main()