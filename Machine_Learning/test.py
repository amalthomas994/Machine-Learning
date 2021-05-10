from operator import le
from Math.Linear_Regression import Stats
from Math.Gradient_Descent import gradient_descent
from GUI import draw
import numpy

learning_rate = 0.05
#house size
x = numpy.array([1100, 1400, 1425, 1550, 1600, 1700, 1700, 1875, 2350, 2450])
#house price
y = numpy.array([199000, 245000, 319000, 240000, 312000, 279000, 310000, 308000, 405000, 324000])
# y = y * 15

def main():
    linespace = numpy.linspace(min(x)-2, max(x)+2)
    data = {
                    'x': x,
                    'y': y
                }
    xx = gradient_descent.GradientDescent(data, learning_rate)
    x_new, y_new = xx.standardize_data_min_max(xx.data['x'], xx.data['y'])
    stat = Stats.Statistics()
    m = stat.regressionSlope(x_new,y_new)
    b = stat.regressionYintercept(x_new, y_new)
    linespace = numpy.linspace(min(x_new)-2, max(x_new)+2)
    
    print(f"Regression Line: y = {m}x + {b}")
    regression_line = f'y = {m}x + {b}'
    
    
    data = {
        'Config':
            {
                'width': 1000,
                'height': 1000,
                'dpi': 100
            },
        'Data':
        {
            'Scatter':
                [{
                    'x': x,
                    'y': y
                }],    
            'Line':
                [{
                    'x': linespace,
                    'y': (m*linespace)+b
                }],
            'Regression Line': regression_line

        }            
    }
    
    plot_1 = draw.Plotter(data)
    plot_1.run()
    gd_data = data["Data"]["Scatter"][0]
    des = gradient_descent.GradientDescent(gd_data, learning_rate)
    error, m_pred, b_pred, linespace_pred, x_pred, y_pred = des.descent()
    regression_line = f'y = {m_pred}x + {b_pred}'
    
    print(linespace_pred)
    data_pred = {
        'Config':
            {
                'width': 1000,
                'height': 1000,
                'dpi': 100
            },
        'Data':
        {
            'Scatter':
                [{
                    'x': x_pred,
                    'y': y_pred
                }],    
            'Line':
                [{
                    'x': linespace_pred,
                    'y': (m_pred*linespace_pred)+b_pred
                },
                {
                    'x': linespace_pred,
                    'y': (m*linespace_pred)+b
                }],
            'Regression Line': regression_line

        }            
    }
    plot = draw.Plotter(data_pred)
    plot.run()

if __name__ == "__main__":
    main()
