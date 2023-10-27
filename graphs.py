import matplotlib.dates as mdates
from matplotlib.figure import Figure


def graph_sims_and_obs_matplotlib(
    sims, obs, ID, sims_data_name="simulation_timeseries", obs_data_name="obsdis"
):
    # observations, simulations, time
    observations = obs.sel(station=ID)[obs_data_name].values
    simulations = sims.sel(station=ID)[sims_data_name].values
    time = obs.sel(station=ID).time.values

    # Create the Matplotlib figure and axes
    fig = Figure(figsize=(12, 5))
    ax = fig.add_subplot(111)

    # Plot the data
    ax.plot(time, simulations, color="#34eb7d", label="simulations")
    ax.plot(time, observations, color="#3495eb", label="observations")

    # Configure the plot
    ax.set_title("Simulations & Observations")
    ax.set_ylabel("discharge")
    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%Y-%m-%d")
    )  # Format the x-axis to show dates
    ax.legend()

    return fig
