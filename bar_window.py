from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import os

FILE = 'F:\\Dev\\Python\\TwitchEmoteBars\\emote_bars.html'

class TransparentWebEngineView(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(TransparentWebEngineView, self).__init__(*args, **kwargs)
        self.page().setBackgroundColor(QtCore.Qt.transparent)

app = QtWidgets.QApplication([])
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # Enable high DPI scaling
app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)  # Use high DPI icons

# Create a main window
mainWindow = QtWidgets.QMainWindow()
mainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)  # Enable transparency

# Create a WebEngineView
webView = TransparentWebEngineView()

# Load an HTML file
webView.load(QtCore.QUrl.fromLocalFile(os.path.abspath(FILE)))

# Set the WebEngineView as the central widget of the main window
mainWindow.setCentralWidget(webView)

# Resize the window
mainWindow.resize(800, 600)
mainWindow.show()

app.exec_()

