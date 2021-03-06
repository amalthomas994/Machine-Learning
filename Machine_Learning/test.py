from Math.Linear_Regression import Stats
from GUI import draw
import numpy

x = numpy.array([1, 3, 5, 6, 9, 10, 17, 18, 19, 26])
y = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = y * 15

def main():
    stat = Stats.Statistics()
    m = stat.regressionSlope(x,y)
    b = stat.regressionYintercept(x, y)
    linespace = numpy.linspace(min(x)-2, max(x)+2)
    
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
                {
                    'x': x,
                    'y': y
                },    
            'Line':
                {
                    'x': linespace,
                    'y': (m*linespace)+b
                },
            'Regression Line': regression_line

        }            
    }
    
    plot = draw.Plotter(data)
    plot.run()

if __name__ == "__main__":
    main()
