import matplotlib.pyplot as plt

def plot_graph(data, 
               title='Graph', 
               x_label='X', 
               y_label='Y'):
    """
    Plot a graph based on the provided data.

    Parameters:
    - data (dict): A dictionary containing the data for the graph. Keys represent x-values and values represent y-values.
    - title (str): The title of the graph (optional, default='Graph').
    - x_label (str): The label for the x-axis (optional, default='X').
    - y_label (str): The label for the y-axis (optional, default='Y').

    Returns:
    - fig (matplotlib.figure.Figure): The Figure object containing the plotted graph.
    """

    # Input validation
    if not isinstance(data, dict):
        raise ValueError("Invalid data type. Expected dict.")
    if not all(isinstance(key, (int, float)) and isinstance(value, (int, float)) for key, value in data.items()):
        raise ValueError("Invalid data format. Expected numeric values in the data dictionary.")

    # Create the figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Plot the data
    ax.plot(list(data.keys()), list(data.values()))

    # Set the graph title, x-axis label, and y-axis label
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    return fig