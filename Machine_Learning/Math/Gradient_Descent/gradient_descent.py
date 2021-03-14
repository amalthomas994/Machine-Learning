import numpy



class GradientDescent:
    def __init__(self, data, learning_rate):
        print('Starting Gradient Descent Class')
        self.data = data
        self.learning_rate = learning_rate
        self.descent()

    def descent():  
        x_actual = self.data['Scatter']['x']
        y_actual = self.data['Scatter']['y']
        self.standardize_data(x_actual, y_actual)
    def standardize_data(x, y):
        





#y_predicted = m_predicted * x + b_predicted
#Predicted Linear Line
#1. Initialize with random m_predicted and b_predicted values
m_predicted = numpy.random.randint(100)
b_predicted = numpy.random.randint(100)
y_predicted_array = []
for value in x:
    y_predicted = (m_predicted*value) + b_predicted
    y_predicted_array.append(y_predicted)
print(y_predicted_array)

#Prediction Error
#sum of squared errors (SSE)
#0.5*(actual - predicted)^2
sse = 0
print(zip(y_predicted_array, y))
for y, y_actual in zip(y_predicted_array, y):
    sse = (0.5*numpy.power((y_actual - y), 2)) + sse
print(sse)

#error gradient
learning_rate = 0.05
#house size
x = numpy.array([1100, 1400, 1425, 1550, 1600, 1700, 1700, 1875, 2350, 2450])
#house price
y = numpy.array([199000, 245000, 319000, 240000, 312000, 279000, 310000, 308000, 405000, 324000])
# y = y * 15
y_max = numpy.amax(y)
x_max = numpy.amax(x)

max_min = numpy.array([y_max, x_max])
max_min = numpy.amax(max_min)

data = {
        
    'Scatter':
        {
            'x': x,
            'y': y
        },    
    }
def main():
    gd = GradientDescent(data, learning_rate)
if __name__ == "__main__":
    main()
