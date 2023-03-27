# F1 Tel Data Plotter
This Python script utilizes the fastf1 library to plot the telemetry data for the top three podium finishers of a given F1 race. The user can specify the year of the event, the location of the event, and the session type (e.g., qualifying or race) through command-line arguments.

### Requirements
- Python 3.x
- `matplotlib` library
- `fastf1` library

### Usage
To run the script, navigate to the directory where the script is saved and execute the following command in the terminal:
```
python f1_tel_data_plotter.py -y YEAR -e EVENT -s SESSION
```
where `YEAR` is the year of the event, `EVENT` is the location of the event (e.g., "Monaco" or "Australia"), and `SESSION` is the session type (e.g., "Q" for qualifying or "R" for race).

### Output
The script will generate five subplots, each representing a different telemetry data field (RPM, speed, throttle, brake, and gear number) plotted against the distance traveled for the top three podium finishers of the specified event. The subplots share the same x-axis, which represents the distance traveled in meters. Each driver's line plot is color-coded by their team color, and a legend is included for each subplot to identify the drivers.