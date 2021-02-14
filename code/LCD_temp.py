# Import necessary libraries for commuunication and display use
import lcddriver
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 14

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to display")
        display.lcd_display_string("Hell dear, Max", 1)  # Write line of text to first line of display
        display.lcd_display_string("Hell dear, Sergey", 2)  # Write line of text to second line of display
        time.sleep(4)                                     # Give time for the message to be read
        display.lcd_clear() 
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            display.lcd_display_string("Temp={0:0.1f}*C".format(temperature),1)
            display.lcd_display_string("Humidity={0:0.1f}%".format(humidity),2)

            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
        
        
        display.lcd_clear()                               # Clear the display of any data       
        display.lcd_display_string("Go to sleep!", 1)    # Refresh the first line of display with a different message
        time.sleep(4)                                     # Give time for the message to be read
        display.lcd_clear()                               # Clear the display of any data
        time.sleep(2)                                     # Give time for the message to be read

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()