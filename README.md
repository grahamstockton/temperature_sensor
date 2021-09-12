# temperature_sensor
Arduino temperature sensor. Will become a PID controller once transistors arrive from China.

Notes on use:
-This code is designed to be used with an arduino/elegoo uno R3 or similar, with a LM35 temperature sensor plugged into the analog 0 port. The uno will need to be connected to your computer for the entire duration of the program.
-The serial channel used here is "COM4", but will likely be different for your device. You can use a variety of methods to check which channel to use, but I just checked in the arduino IDE when the uno was plugged in.
