import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from gui.window_keyboard import Ui_MainWindow as keyboard_window

LOWER = "QPushButton\n""{\n" \
			"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"" \
			""    border: 1px solid gray;\n" \
			"    border-radius: 2px;\n" \
			"}\n" \
			"\n" \
			"QPushButton:pressed \n" \
			"{    \n" \
			"    background-color: rgb(140, 223, 255);\n" \
			" }"

UPPER = "QPushButton\n""{\n" \
			"    background-color: rgb(0, 162, 255);\n"" \
			""    border: 1px solid gray;\n" \
			"    border-radius: 2px;\n" \
			"}\n" \
			"\n" \
			"QPushButton:pressed \n" \
			"{    \n" \
			"    background-color: rgb(140, 223, 255);\n" \
			" }"


class KeyboardWindow(QMainWindow, keyboard_window):

	def __init__(self, callback=None, parent=None):
		super(KeyboardWindow, self).__init__(parent)
		QMainWindow.__init__(self, parent)
		self.setupUi(self)

		# self.setFixedSize(self.size())
		self.setWindowFlags(Qt.WindowCloseButtonHint)
		# self.setWindowFlags(Qt.FramelessWindowHint)
		self.setWindowModality(Qt.ApplicationModal)

		self.buttons = [
			self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9, self.btn_0,
			self.btn_q, self.btn_w, self.btn_e, self.btn_r, self.btn_t, self.btn_y, self.btn_u, self.btn_i, self.btn_o, self.btn_p,
			self.btn_a, self.btn_s, self.btn_d, self.btn_f, self.btn_g, self.btn_h, self.btn_j, self.btn_k, self.btn_l,
			self.btn_z, self.btn_x, self.btn_c, self.btn_v, self.btn_b, self.btn_n, self.btn_m,
			self.btn_upper, self.btn_underscore, self.btn_at, self.btn_space, self.btn_period, self.btn_backspace, self.btn_ok
		]

		self.cb = callback
		self.upper = False
		self.keys = ''

		self.setup_listener()

	def setup_listener(self):

		self.btn_1.clicked.connect(self.btn_1_clicked)
		self.btn_2.clicked.connect(self.btn_2_clicked)
		self.btn_3.clicked.connect(self.btn_3_clicked)
		self.btn_4.clicked.connect(self.btn_4_clicked)
		self.btn_5.clicked.connect(self.btn_5_clicked)
		self.btn_6.clicked.connect(self.btn_6_clicked)
		self.btn_7.clicked.connect(self.btn_7_clicked)
		self.btn_8.clicked.connect(self.btn_8_clicked)
		self.btn_9.clicked.connect(self.btn_9_clicked)
		self.btn_0.clicked.connect(self.btn_0_clicked)

		self.btn_a.clicked.connect(self.btn_a_clicked)
		self.btn_b.clicked.connect(self.btn_b_clicked)
		self.btn_c.clicked.connect(self.btn_c_clicked)
		self.btn_d.clicked.connect(self.btn_d_clicked)
		self.btn_e.clicked.connect(self.btn_e_clicked)
		self.btn_f.clicked.connect(self.btn_f_clicked)
		self.btn_g.clicked.connect(self.btn_g_clicked)
		self.btn_h.clicked.connect(self.btn_h_clicked)
		self.btn_i.clicked.connect(self.btn_i_clicked)
		self.btn_j.clicked.connect(self.btn_j_clicked)
		self.btn_k.clicked.connect(self.btn_k_clicked)
		self.btn_l.clicked.connect(self.btn_l_clicked)
		self.btn_m.clicked.connect(self.btn_m_clicked)
		self.btn_n.clicked.connect(self.btn_n_clicked)
		self.btn_o.clicked.connect(self.btn_o_clicked)
		self.btn_p.clicked.connect(self.btn_p_clicked)
		self.btn_q.clicked.connect(self.btn_q_clicked)
		self.btn_r.clicked.connect(self.btn_r_clicked)
		self.btn_s.clicked.connect(self.btn_s_clicked)
		self.btn_t.clicked.connect(self.btn_t_clicked)
		self.btn_u.clicked.connect(self.btn_u_clicked)
		self.btn_v.clicked.connect(self.btn_v_clicked)
		self.btn_w.clicked.connect(self.btn_w_clicked)
		self.btn_x.clicked.connect(self.btn_x_clicked)
		self.btn_y.clicked.connect(self.btn_y_clicked)
		self.btn_z.clicked.connect(self.btn_z_clicked)

		self.btn_upper.clicked.connect(self.btn_upper_clicked)
		self.btn_underscore.clicked.connect(self.btn_underscore_clicked)
		self.btn_at.clicked.connect(self.btn_at_clicked)
		self.btn_space.clicked.connect(self.btn_space_clicked)
		self.btn_period.clicked.connect(self.btn_period_clicked)
		self.btn_backspace.clicked.connect(self.btn_backspace_clicked)
		self.btn_ok.clicked.connect(self.btn_ok_clicked)

	def btn_1_clicked(self):
		self.keys += self.btn_1.text()
		self.reflect_keys()

	def btn_2_clicked(self):
		self.keys += self.btn_2.text()
		self.reflect_keys()

	def btn_3_clicked(self):
		self.keys += self.btn_3.text()
		self.reflect_keys()

	def btn_4_clicked(self):
		self.keys += self.btn_4.text()
		self.reflect_keys()

	def btn_5_clicked(self):
		self.keys += self.btn_5.text()
		self.reflect_keys()

	def btn_6_clicked(self):
		self.keys += self.btn_6.text()
		self.reflect_keys()

	def btn_7_clicked(self):
		self.keys += self.btn_7.text()
		self.reflect_keys()

	def btn_8_clicked(self):
		self.keys += self.btn_8.text()
		self.reflect_keys()

	def btn_9_clicked(self):
		self.keys += self.btn_9.text()
		self.reflect_keys()

	def btn_0_clicked(self):
		self.keys += self.btn_0.text()
		self.reflect_keys()

	def btn_a_clicked(self):
		self.keys += self.btn_a.text()
		self.reflect_keys()

	def btn_b_clicked(self):
		self.keys += self.btn_b.text()
		self.reflect_keys()

	def btn_c_clicked(self):
		self.keys += self.btn_c.text()
		self.reflect_keys()

	def btn_d_clicked(self):
		self.keys += self.btn_d.text()
		self.reflect_keys()

	def btn_e_clicked(self):
		self.keys += self.btn_e.text()
		self.reflect_keys()

	def btn_f_clicked(self):
		self.keys += self.btn_f.text()
		self.reflect_keys()

	def btn_g_clicked(self):
		self.keys += self.btn_g.text()
		self.reflect_keys()

	def btn_h_clicked(self):
		self.keys += self.btn_h.text()
		self.reflect_keys()

	def btn_i_clicked(self):
		self.keys += self.btn_i.text()
		self.reflect_keys()

	def btn_j_clicked(self):
		self.keys += self.btn_j.text()
		self.reflect_keys()

	def btn_k_clicked(self):
		self.keys += self.btn_k.text()
		self.reflect_keys()

	def btn_l_clicked(self):
		self.keys += self.btn_l.text()
		self.reflect_keys()

	def btn_m_clicked(self):
		self.keys += self.btn_m.text()
		self.reflect_keys()

	def btn_n_clicked(self):
		self.keys += self.btn_n.text()
		self.reflect_keys()

	def btn_o_clicked(self):
		self.keys += self.btn_o.text()
		self.reflect_keys()

	def btn_p_clicked(self):
		self.keys += self.btn_p.text()
		self.reflect_keys()

	def btn_q_clicked(self):
		self.keys += self.btn_q.text()
		self.reflect_keys()

	def btn_r_clicked(self):
		self.keys += self.btn_r.text()
		self.reflect_keys()

	def btn_s_clicked(self):
		self.keys += self.btn_s.text()
		self.reflect_keys()

	def btn_t_clicked(self):
		self.keys += self.btn_t.text()
		self.reflect_keys()

	def btn_u_clicked(self):
		self.keys += self.btn_u.text()
		self.reflect_keys()

	def btn_v_clicked(self):
		self.keys += self.btn_v.text()
		self.reflect_keys()

	def btn_w_clicked(self):
		self.keys += self.btn_w.text()
		self.reflect_keys()

	def btn_x_clicked(self):
		self.keys += self.btn_x.text()
		self.reflect_keys()

	def btn_y_clicked(self):
		self.keys += self.btn_y.text()
		self.reflect_keys()

	def btn_z_clicked(self):
		self.keys += self.btn_z.text()
		self.reflect_keys()

	def btn_underscore_clicked(self):
		self.keys += self.btn_underscore.text()
		self.reflect_keys()

	def btn_at_clicked(self):
		self.keys += self.btn_at.text()
		self.reflect_keys()

	def btn_space_clicked(self):
		self.keys += ' '
		self.reflect_keys()

	def btn_period_clicked(self):
		self.keys += self.btn_period.text()
		self.reflect_keys()

	def btn_backspace_clicked(self):
		self.keys = self.keys[:-1]
		self.reflect_keys()

	def btn_ok_clicked(self):
		self.keys = ''
		self.hide()

	def btn_upper_clicked(self):
		self.upper = not self.upper

		if self.upper:
			self.btn_upper.setStyleSheet(UPPER)

			for i in range(10, 36):
				self.buttons[i].setText(self.buttons[i].text().upper())
		else:
			self.btn_upper.setStyleSheet(LOWER)

			for i in range(10, 36):
				self.buttons[i].setText(self.buttons[i].text().lower())

	def reflect_keys(self):
		self.edit_text.setText(self.keys)
		self.edit_text.setFocus()
		if self.cb is not None:
			self.cb.on_key(self.keys)


def main():
	app = QApplication(sys.argv)
	kb_window = KeyboardWindow()
	kb_window.show()

	try:
		while True:
			app.processEvents()

	except KeyboardInterrupt:
		pass
	kb_window.close()
	app.quit()


if __name__ == '__main__':
	main()
