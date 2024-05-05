import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.Qt import Qt

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window transparency
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Create a QWebEngineView widget
        self.browser = QWebEngineView(self)
        # Set the size of the window
        self.browser.resize(600, 600)
        # Load the HTML file
        self.browser.load(QUrl.fromLocalFile("F:\\Dev\\Python\\TwitchEmoteBars\\emote_bars.html"))

        # Set the central widget of the window
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = TransparentWindow()
    mainWin.show()
    sys.exit(app.exec_())
