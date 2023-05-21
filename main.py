from PyQt5.QtWidgets import QApplication
import sys
from UserMainWindow import UserMainWindow

app = QApplication(sys.argv)
window = UserMainWindow()
window.showMaximized()
sys.exit(app.exec())