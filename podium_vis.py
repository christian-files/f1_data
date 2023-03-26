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

    # Creating an accessible dictionary for the podium \
    # that accesses the laps table for each driver.
    # Accessing the team colour as well...
    # driver_dict = {}
    # for driver in podium_abb:
    #     driver_dict[driver] = [race.laps.pick_driver(driver), \
    #     fastf1.plotting.team_color(race.laps.pick_driver(driver).Team.unique()[0])]

    driver_dict = {}
    for driver in podium_abb:
        driver_dict[driver] = [race.laps.pick_driver(driver).pick_fastest().get_car_data().add_distance(), \
        fastf1.plotting.team_color(race.laps.pick_driver(driver).Team.unique()[0])]

    # Plotting top three podiums lap number against time
    fig, ax = plt.subplots()
    for driver in driver_dict:
        ax.plot(driver_dict[driver][0]['Distance'], \
        driver_dict[driver][0]['Speed'], \
        # color=driver_dict[driver][1],
        label=driver)

    ax.set_title(f"Podium Fastest Lap Speed Comparison for {event_name}")
    ax.set_xlabel("Distance m")
    ax.set_ylabel("Speed Km/h")
    ax.legend()
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
