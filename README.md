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

### Example
Running the following code will give you an output shown below:
```
python podium_vis.py -y 2018 -e 'British GP' -s 'R'
```
<img width="1308" alt="image" src="https://user-images.githubusercontent.com/116644174/228486840-eff23087-0fdc-493e-ad93-c4a51f53563f.png">

### Note
Some further modifications are still needed here as the legend is overlapping the visualisations and driver colours do not represent accurately. The driver colour code does exist, but is commented out. This is because there was a clash of colour when two of the same team were in the top three and made the graphs hard to read.
