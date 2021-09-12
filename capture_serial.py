import serial
import sys
import time

# takes temperature samples for a certain duration, and then writes the results to a .csv file
def capture_serial_csv(port_name, output_name="PID_output.csv", measurement_timeout=5):
    # this try block catches the syntaxError that occurs when the arduino is disconnected mid-sample and gives a more descriptive error
    try:
        # set starting time
        start_time = time.time()

        # open output file for writing
        with open(output_name, 'w') as output_file:

            # write everything that gets sent to serial
            with serial.Serial(port_name) as ser:

                # main loop
                while ser:

                    # write csv data to file
                    output_file.write(ser.readline().decode("utf-8"))

                    # exit if measurement_timeout has elapsed
                    if time.time() - start_time >= measurement_timeout:
                        return
                        
    except:
        raise RuntimeError("Error: device connection terminated while taking sample")


# same as capture_serial_csv, but instead writes the data to two lists, which are returned
def capture_serial_list(port_name, measurement_timeout=3): # stores value in list of lists for passing with python -- note that this is sensitive to how we format the data in the .ino file
    try:
        # set a base time
        start_time = time.time()

        # create lists for writing
        time_list = []
        temperature_list = []

        # write everything that gets sent to serial
        with serial.Serial(port_name) as ser:

            # remove labels at beginning
            ser.readline()

            # main loop
            while ser:
                # split arduino output into time, temp values
                serial_tuple = [eval(item) for item in ser.readline().decode("utf-8").split(',')]

                # add each value to list
                time_list.append(serial_tuple[0])
                temperature_list.append(serial_tuple[1])

                # return if measurement_timeout has elapsed
                if time.time() - start_time >= measurement_timeout:
                    return time_list, temperature_list

    except: # Something went wrong
        raise RuntimeError("Error: device connection terminated while taking sample")

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # get data series
    if len(sys.argv) > 1:
        times, temps = capture_serial_list("COM4", sys.argv[1], measurement_timeout=180)
    else:
        times, temps = capture_serial_list("COM4", measurement_timeout=180)

    # plot recorded values
    plt.plot(times, temps)
    plt.title("Temperature vs. Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (C)")
    plt.savefig("temperature_plot.png")