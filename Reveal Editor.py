import sys
# import site
# site.addsitedir('/usr/local/lib/python2.7/site-packages')
from PySide         import QtCore, QtGui, QtWebKit
from PySide.QtGui   import *
from PySide.QtCore  import *

class Reveal(QMainWindow):
	def __init__(self, parent = None):
		super(Reveal, self).__init__(parent)
		view = QtWebKit.QWebView()
		view.load(QtCore.QUrl('./index (copy).html'))
		self.frame = view.page().mainFrame()
		self.setUpToolBar()
		self.setCentralWidget(view)

	def setUpToolBar(self):
		self.toolbar = QToolBar()
		self.addToolBar( Qt.BottomToolBarArea , self.toolbar)
		addDivAction = QAction('add div', self)
		self.toolbar.addAction(addDivAction)
		addDivAction.triggered.connect(self.addDiv)

	def addDiv(self):
		print self.frame.evaluateJavaScript('addTextWidget();')

if __name__ == '__main__':			
	app = QtGui.QApplication(sys.argv)
	Reveal = Reveal()
	Reveal.show()
	sys.exit(app.exec_())