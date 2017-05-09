import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

	def __init__(self, icon, parent=None):
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
		menu = QtWidgets.QMenu(parent)
		exitAction = menu.addAction("Exit")
		self.setContextMenu(menu)
		exitAction.triggered.connect(self.exit) # alternative: QtWidgets.qApp.quit)
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.thirsty)
		self.activated.connect(self.iconActivated)

	def exit(self):
		QtCore.QCoreApplication.exit()

	def thirsty(self):
		self.show()
		self.timer.stop()

	def notThirsty(self):
		self.hide()
		self.timer.start(1000*60*30) # remind every half hour

	def iconActivated(self, reason):
		if reason == QtWidgets.QSystemTrayIcon.Trigger:
			self.notThirsty()

def main():
	app = QtWidgets.QApplication(sys.argv)

	w = QtWidgets.QWidget()
	trayIcon = SystemTrayIcon(QtGui.QIcon("thirsty.png"), w)
	trayIcon.notThirsty()
	
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

# https://stackoverflow.com/questions/893984/pyqt-show-menu-in-a-system-tray-application
# https://ralsina.me/posts/BB974.html
# https://stackoverflow.com/questions/37919169/pyqt-system-tray-icon-exit-when-click-menu-item
