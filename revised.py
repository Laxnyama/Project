import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

	def _init_(self):
		super(Window, self)._int_()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("ToNE")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))


	// Menu bar

		// file option
		extractAction = QtGui.QAction("file saved", self)
		extractAction.setShortcut(Ctrl+Q)
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)

		// edit option
		extractAction = QtGui.QAction("Edit file", self)
		extractAction.setShortcut(Ctrl+Q)
		extractAction.setStatusTip('Edit the file')
		extractAction.triggered.connect(self.close_application)

		// view option
		extractAction = QtGui.QAction("Viewed file", self)
		extractAction.setShortcut(Ctrl+Q)
		extractAction.setStatusTip('View The File')
		extractAction.triggered.connect(self.close_application)

		// help optoin
		extractAction = QtGui.QAction("Help", self)
		extractAction.setShortcut(Ctrl+Q)
		extractAction.setStatusTip('Get Help')
		extractAction.triggered.connect(self.close_application)


		self.statusBar()

		// File
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)

		// Edit
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&Edit')
		fileMenu.addAction(extractAction)

		// View
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&View')
		fileMenu.addAction(extractAction)

		// Help
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&Help')
		fileMenu.addAction(extractAction)






		self.home()

		def home(self):
		btn = QtGui.QpushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0, 100)

	// edge tool
		extractAction = QtGui.QAction(QtGui.QIcon('lindaEdge.jpg'), 'Drag and drop', self)
		extractAction.triggered.connect(self.close_application)

		self.toolBar = self.addToolBar("Edge")
		self.toolBar.addAction(extractAction)

	// node tool
		extractAction = QtGui.QAction(QtGui.QIcon('lindaNode.jpg'), 'Drag and drop', self)
		extractAction.triggered.connect(self.close_application)

		self.toolBar = self.addToolBar("Node")
		self.toolBar.addAction(extractAction)





		self.show()

	def close_application(self):
		choice = QtGui.QmessageBox.question(self, 'Exctract!', "Are you sure?", QtGui.QMessageBox.No)

		if choice == QtGui.QMessageBox.Yes:
			print("Extracting  lood")
			sys.exit()
		else:
			pass





	def run():
		app = QtGui.QApplication(sys.argv)
		GUI = Window()
		sys.exit(app.exec_())
