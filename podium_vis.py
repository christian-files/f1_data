#!/usr/bin/env python

# Import libraries
import matplotlib.pyplot as plt
import fastf1 as ff
import fastf1.plotting
import os
import argparse

def plot_tel_data(year, location, session):
        # Setup cache for faster data loading
    if not os.path.exists('cache'):
        os.mkdir('cache')
        print('Made directory "cachce" to use caching...')
    ff.Cache.enable_cache('cache')

    # Enable some matplotlib patches for plotting timedelta values and load
    # FastF1's default color scheme
    ff.plotting.setup_mpl()

    # Load in race session
    race = ff.get_session(year, location, session)
    race.load()

    # Get event name
    event_name = race.event['EventName']

    # Get top podium abbreviations
    podium_abb = race.results['Abbreviation'][0:3]

    driver_dict = {}
    for driver in podium_abb:
        driver_dict[driver] = [race.laps.pick_driver(driver).pick_fastest().get_car_data().add_distance(), \
        fastf1.plotting.team_color(race.laps.pick_driver(driver).Team.unique()[0])]

    # Plotting top three podiums lap number against time
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, sharex=True)
    for driver in driver_dict:
        ax1.plot(driver_dict[driver][0]['Distance'], \
        driver_dict[driver][0]['RPM'], \
        # color=driver_dict[driver][1],
        label=driver)
        ax2.plot(driver_dict[driver][0]['Distance'], \
        driver_dict[driver][0]['Speed'], \
        # color=driver_dict[driver][1],
        label=driver)
        ax3.plot(driver_dict[driver][0]['Distance'], \
        driver_dict[driver][0]['Throttle'], \
        # color=driver_dict[driver][1],
        label=driver)
        ax4.plot(driver_dict[driver][0]['Distance'], \
        driver_dict[driver][0]['Brake'], \
        # color=driver_dict[driver][1],
        label=driver)
        ax5.plot(driver_dict[driver][0]['Distance'], \
        driver_dict[driver][0]['nGear'], \
        # color=driver_dict[driver][1],
        label=driver)

    ax1.set_ylabel("RPM")
    ax1.legend()

    ax2.set_ylabel("Speed Km/h")
    ax2.legend()

    ax3.set_ylabel("Throttle %")
    ax3.legend()

    ax4.set_ylabel("Brake %")
    ax4.legend()

    ax5.set_xlabel("Distance m")
    ax5.set_ylabel("nGear")
    ax5.legend()

    # Setting title
    ax1.set_title(f"{event_name} {year} Telemetry")

    # Adjust the layout to avoid overlapping labels
    plt.tight_layout()

    # Show the plots
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-y",
        "--year",
        nargs=1,
        type=int,
        help="Year of event",
        required=True)

    parser.add_argument(
        "-e",
        "--event",
        nargs=1,
        type=str,
        help="Event Location",
        required=True)

    parser.add_argument(
        "-s",
        "--session",
        nargs=1,
        type=str,
        help="Select Event (E.g. 'Q' or 'R')",
        required=True)

    args = parser.parse_args()

    event_year = args.year[0]
    event_location = args.event[0]
    session_type = args.session[0]

    plot_tel_data(event_year, event_location, session_type)
