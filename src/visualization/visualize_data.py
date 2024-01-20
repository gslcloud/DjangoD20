import matplotlib.pyplot as plt
import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError("File not found!")

def visualize_data(data, x_column, y_column, plot_type='bar', save_as=None):
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError("Invalid column names!")

    if plot_type == 'bar':
        plt.bar(data[x_column], data[y_column])
    elif plot_type == 'line':
        plt.plot(data[x_column], data[y_column])
    elif plot_type == 'scatter':
        plt.scatter(data[x_column], data[y_column])
    elif plot_type == 'hist':
        plt.hist(data[x_column], bins=10)
    else:
        raise ValueError("Invalid plot type!")

    plt.xlabel(x_column)
    plt.ylabel(y_column)

    if save_as:
        plt.savefig(save_as)
    else:
        plt.show()

if __name__ == "__main__":
    file_path = "data.csv"
    x_column = "x"
    y_column = "y"

    data = load_data(file_path)
    visualize_data(data, x_column, y_column, plot_type='bar')