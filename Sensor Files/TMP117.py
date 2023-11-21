# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import adafruit_tmp117
import digitalio

# Initialize I2C and TMP117 sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
tmp117 = adafruit_tmp117.TMP117(i2c)

# Initialize the push button
button_pin = digitalio.DigitalInOut(board.D23)  # Replace D23 with the actual GPIO pin connected to the button
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP

# Open the file for writing
file1 = open("myfile.txt", "w")

def main():
    recording = False
    start_time = 0

    try:
        while True:
            if button_pin.value and not recording:
                recording = True
                start_time = time.monotonic()
                print("Recording started.")

            if recording:
                elapsed_time = time.monotonic() - start_time
                temperature = tmp117.temperature
                print("Time: %.2f seconds, Temperature: %.2f degrees C" % (elapsed_time, temperature))
                file1.write("%.2f, %.2f\n" % (elapsed_time, temperature))
                file1.flush()  # Flush the buffer to make sure data is written to the file immediately

            if recording and not button_pin.value:
                recording = False
                print("Recording stopped.")
                start_time = 0

            time.sleep(0.1)  # This prevents busy waiting

    except KeyboardInterrupt:
        pass
    finally:
        file1.close()

if __name__ == "__main__":
    main()
