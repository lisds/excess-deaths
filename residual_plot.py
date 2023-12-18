
import matplotlib.pyplot as plt

def plot_with_errors(x_values, y_values, c, s):
    
    predicted = c + s * x_values
    
    errors = y_values - predicted
    
    plt.plot(x_values, y_values, 'o', color='blue')
    plt.plot(x_values, predicted, 'o', color='red')
    
    for i in np.arange(len(x_values)):
        x = x_values[i]
        y_0 = predicted[i]
        y_1 = y_values[i]
        plt.plot([x, x], [y_0, y_1], ':', color='black', linewidth=1)
    return np.sqrt(np.mean(errors ** 2))

