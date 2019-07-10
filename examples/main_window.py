import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from gui.keyboard_window import KeyboardWindow
from gui.window_main import Ui_main_window as main_window


class MainWindow(QMainWindow, main_window):

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		QMainWindow.__init__(self, parent)
		self.setupUi(self)

		# create an instance of the Keyboard
		# add self as a parameter for callback
		self.kb = KeyboardWindow(callback=self)

		self.focused_input = None

		# initialize click event on the input
		# for calling keyboard popup
		self.lineEdit.mousePressEvent = self.lineEdit_clicked

	def lineEdit_clicked(self, e):
		self.focused_input = self.lineEdit
		self.kb.show()

	def on_key(self, keys):
		if self.focused_input is not None:
			self.focused_input.setText(keys)


def main():
	app = QApplication(sys.argv)
	m_window = MainWindow(None)
	m_window.show()

	try:
		while True:
			app.processEvents()

	except KeyboardInterrupt:
		pass
	m_window.close()
	app.quit()


if __name__ == '__main__':
	main()
