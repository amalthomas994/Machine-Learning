import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy
import json
import traceback
import logging
import qdarkstyle
logging.basicConfig(level=logging.INFO)

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
class plotCanvas(FigureCanvasQTAgg):
    def __init__(self, width, height, dpi):
        figure = Figure(figsize=(width, height), dpi=dpi)
        figure.set_facecolor('grey')
        figure.set_edgecolor('red')
        self.fig = figure.subplots()
        super().__init__(figure)
        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, widget):
        super().__init__()
        
        logging.info('Creating Main Window')
        # self.resize(1000, 1000)
        self.setWindowIcon(QtGui.QIcon('favicon.png'))
        self.setWindowTitle('Linear Regression')
        self.setCentralWidget(widget)
        self.show()
    
    def contextMenuEvent(self, event):
        cmenu = QtWidgets.QMenu(self)

        quitAction = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == quitAction:
            QtWidgets.qApp.quit()


class Plotter():
    def __init__(self, info):
        print('Starting Plotter')
        self.info = info
        self.config = None
        self.data = None
        self.parseData(self.info)
    
    def parseData(self, info):
        for item in info.keys():
            if item == 'Config':
                self.config = info[item]
                self.width = info[item]['width']
                self.height = info[item]['height']
                self.dpi = info[item]['dpi']
            
            if item == 'Data':
                self.data = info[item]
            
    def run(self):
        application = QtWidgets.QApplication(sys.argv)
        application.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        canvas = plotCanvas(self.width, self.height, self.dpi)
        canvas.fig.set_title('Linear Regression')
        canvas.fig.set_xlabel('x')
        canvas.fig.set_ylabel('y')
        # canvas.fig.set_facecolor("grey")
        # canvas.fig.set_edgecolor("red")
        
        if self.data['Scatter']:
            scatter_data = self.data['Scatter']
            canvas.fig.scatter(scatter_data['x'], scatter_data['y'], marker='o')
        if self.data['Line']:
            line_data = self.data['Line']
            canvas.fig.plot(line_data['x'], line_data['y'])
        if self.data['Regression Line']:
            regression_line = self.data['Regression Line']
        

        widget = Widget()
        verticalBox = QtWidgets.QVBoxLayout()
        exitButton = QtWidgets.QPushButton('Exit')
        exitButton.setToolTip('Exit the Application')
        exitButton.clicked.connect(self.exitAction)
        regression_equation = QtWidgets.QLabel(f'Regression Line Equation: {regression_line}')
        regression_equation.setAlignment(QtCore.Qt.AlignCenter)
        # verticalBox.addWidget(canvas)
        verticalBox.addWidget(regression_equation)
        verticalBox.addWidget(exitButton)

        fig = plt.figure()
        plt.rcParams.update({
        "axes.facecolor": "white",
        "axes.edgecolor": "lightgray",
        "grid.color": "black",
        })
        newCan = FigureCanvasQTAgg(fig)
        figs = fig.add_subplot(111)
        
        figs.plot(line_data['x'], line_data['y'])
        verticalBox.addWidget(newCan) 
        widget.setLayout(verticalBox)
        

    
        window = MainWindow(widget)
        application.exec_()

    def exitAction(self):
        print("Exiting Application")
        QtWidgets.qApp.quit()



