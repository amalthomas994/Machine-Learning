import math
import matplotlib.pyplot as plt
import numpy
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg
from matplotlib.figure import Figure

class Statistics():
    def __init__(self):
        print('Starting BasicMath Class')

    def mean(self, data):
        meanVal = None
        try:
            sum = 0
            for value in data:
                sum = sum + value
            meanVal = sum/len(data)
        except Exception as ex:
            print(f'Exception: {ex}')

        return meanVal
    def standardDeviation(self, data):
        sum = 0
        mean = self.mean(data)
        for value in data:
            sum = sum + (value - mean) ** 2
        stDeviation = math.sqrt(sum/(len(data)-1))
        return stDeviation
    def covariance(self, data1, data2):
        sum = 0
        mean1 = self.mean(data1)
        mean2 = self.mean(data2)
        for value1, value2 in zip(data1, data2):
            sum = sum + ((value1 - mean1)*(value2 - mean2))
        covariance = sum/(len(data1)-1)
        return covariance
    def corrCoefficient(self, data1, data2):
        covXY = self.covariance(data1, data2)
        stDeviationX = self.standardDeviation(data1)
        stDeviationY = self.standardDeviation(data2)
        corrCoeff = covXY/(stDeviationX*stDeviationY)
        return corrCoeff
    def regressionSlope(self, data1, data2):
        stDeviationX = self.standardDeviation(data1)
        stDeviationY = self.standardDeviation(data2)
        corrCoeff = self.corrCoefficient(data1, data2)
        slope = corrCoeff * (stDeviationY/stDeviationX)
        return slope
    def regressionYintercept(self, data1, data2):
        meanY = self.mean(data2)
        meanX = self.mean(data1)
        slope = self.regressionSlope(data1, data2)
        b = meanY - (slope*meanX)
        return b
# x = [17, 13, 12, 15, 16, 14, 16, 16, 18, 19]
# y = [94, 73, 59, 80, 93, 85, 66, 79, 77, 91]

# plt.plot(x, y)
# stat = Statistics()
# print(stat.mean(x))
# print(stat.standardDeviation(x))
# print(stat.mean(y))
# print(stat.standardDeviation(y))