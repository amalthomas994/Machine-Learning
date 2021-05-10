import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.append(path)
from Math.Linear_Regression import Stats
from GUI import draw
import numpy



class GradientDescent:
    def __init__(self, data, learning_rate):
        print('Starting Gradient Descent Class')
        self.data = data
        self.learning_rate = learning_rate
        # self.descent()

    def descent(self):  
        x_actual = self.data['x']
        y_actual = self.data['y']
        x_standardized, y_standardized = self.standardize_data_min_max(x_actual, y_actual)
        # print(x_standardized, y_standardized)
        m_predicted = numpy.random.randint(1)
        b_predicted = numpy.random.randint(1)
        m_predicted = 0.75
        b_predicted = 0.45
        error, m, b, linespace = self.SSE(x_standardized, y_standardized, m_predicted, b_predicted)
        print("The SSE error is " + str(error))
        return error, m, b, linespace, x_standardized, y_standardized
    def standardize_data_min_max(self, x, y):
        y_max = numpy.amax(y)
        y_min = numpy.amin(y)
        x_max = numpy.amax(x)
        x_min = numpy.amin(x)
        x_standardized = []
        y_standardized = []
        for x, y in zip(x, y):
            x_standardized.append((x-x_min)/(x_max-x_min))
            y_standardized.append((y-y_min)/(y_max-y_min))
        return x_standardized, y_standardized
    
    def SSE(self, x, y, m_predicted, b_predicted):
        x_new = x
        y_old = y
        error = 0
        y_new = []
        for x, y in zip(x, y):
            y_predicted = b_predicted + (m_predicted*x)
            print("Y Predicted (" + str(round(x,2)) + ", " + str(round(y,2)) + "): " + str(round(y_predicted,2)) + " Prediction Error: " + str(round(0.5*((y - y_predicted)**2), 3)))
            error = error + 0.5*((y - y_predicted)**2)
            y_new.append(y_predicted)
        x = x_new
        stat = Stats.Statistics()
        m = stat.regressionSlope(x,y_new)
        b = stat.regressionYintercept(x, y_new)
        linespace = numpy.linspace(min(x)-2, max(x)+2)
        
        # print(f"Regression Line: y = {m}x + {b}")
        # regression_line = f'y = {m}x + {b}'
        # data = {
        #     'Config':
        #         {
        #             'width': 1000,
        #             'height': 1000,
        #             'dpi': 100
        #         },
        #     'Data':
        #     {
        #         'Scatter':
        #             {
        #                 'x': x,
        #                 'y': y_old
        #             },    
        #         'Line':
        #             {
        #                 'x': linespace,
        #                 'y': (m*linespace)+b
        #             },
        #         'Regression Line': regression_line

        #     }            
        # }
        
        # plot = draw.Plotter(data)
        # plot.run()
        return error, m, b, linespace



# class CostFunction:
#     def __init__(self):
#         pass
#     def MeanSquaredError(self):
#         pass
# #y_predicted = m_predicted * x + b_predicted
# #Predicted Linear Line
# #1. Initialize with random m_predicted and b_predicted values
# m_predicted = numpy.random.randint(100)
# b_predicted = numpy.random.randint(100)
# y_predicted_array = []
# for value in x:
#     y_predicted = (m_predicted*value) + b_predicted
#     y_predicted_array.append(y_predicted)
# print(y_predicted_array)


# #Prediction Error
# #sum of squared errors (SSE)
# #0.5*(actual - predicted)^2
# sse = 0
# print(zip(y_predicted_array, y))
# for y, y_actual in zip(y_predicted_array, y):
#     sse = (0.5*numpy.power((y_actual - y), 2)) + sse
# print(sse)

