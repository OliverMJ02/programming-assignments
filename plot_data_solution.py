# solution cell
### BEGIN SOLUTION
from matplotlib.figure import Figure


def plot_data(inpl: list[float]) -> Figure:
    fig = Figure()
    axes = fig.gca()
    x_axis: list[int] = []
    for i in range(5, len(inpl) + 5):
        x_axis.append(i)
    axes.plot(x_axis, inpl, color="b", linewidth="2")
    axes.set_ylabel("# Misclustered Nodes")
    axes.set_xlabel("n")
    axes.set_title("# Misclustered Nodes / # nodes")
    axes.set_xlim(5)
    axes.set_ylim(0)
    fig.savefig("plot.png")
    return fig


### END SOLUTION
