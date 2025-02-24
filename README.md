# MicroPython-based PIN Entry System

This project is a PIN entry system built using a Raspberry Pi Pico, MicroPython, and an OLED display. It allows secure PIN input using push buttons, providing a simple yet effective security mechanism for any project requiring user authentication.


![PIN Entry System](https://www.ericbzotti.com/wp-content/uploads/2025/02/WhatsApp-Image-2025-02-23-at-22.18.53-1-1024x768.jpeg)


## Components Used:
- **Raspberry Pi Pico**: A microcontroller with sufficient GPIO pins for input and display.
- **OLED Display (128x64)**: To display the PIN input and status.
- **Push Buttons**: Used for entering the PIN.
- **MicroPython**: The software framework for controlling the Raspberry Pi Pico.
- **LEDs**: Green and Red LEDs to indicate success and failure.

## Features:
- Secure PIN entry using push buttons.
- OLED display shows the entered PIN (masked) and feedback messages.
- Indicator LEDs for success (green) and error (red).
- Simple yet effective for any small security-based project.

## Requirements:
1. **Hardware**:
   - Raspberry Pi Pico
   - OLED display (128x64 SSD1306)
   - Push buttons
   - Green LED (for success)
   - Red LED (for error)
   - Jumper wires and breadboard for connections

2. **Software**:
   - [MicroPython](https://micropython.org/download/rp2-pico/) installed on Raspberry Pi Pico
   - [Thonny IDE](https://thonny.org/) for writing and deploying MicroPython code

## Wiring:

| Raspberry Pi Pico Pin   | Component             | Description                                                 | Additional Connections                                                                                   |
|-------------------------|-----------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| GPIO 14 (Pin 19)        | SDA (OLED Display)    | Data line for I2C communication with OLED display            | Connect to OLED SDA pin, Ground to GND, +3.3V to VCC                                                      |
| GPIO 15 (Pin 21)        | SCL (OLED Display)    | Clock line for I2C communication with OLED display           | Connect to OLED SCL pin, Ground to GND, +3.3V to VCC                                                      |
| GPIO 13 (Pin 13)        | Green LED             | Indicator LED for success (flashes green)                    | Connect an appropriate resistor (220Ω-330Ω) in series with the LED’s anode (positive leg); cathode to GND    |
| GPIO 12 (Pin 12)        | Red LED               | Indicator LED for errors (flashes red)                       | Connect an appropriate resistor (220Ω-330Ω) in series with the LED’s anode (positive leg); cathode to GND    |
| GPIO 16 (Pin 21)        | Button (Up)           | Button to increment the selected digit                       | One side of the button to GPIO 16, the other to GND (with internal pull-up resistor enabled in the code)    |
| GPIO 17 (Pin 22)        | Button (Down)         | Button to decrement the selected digit                       | One side of the button to GPIO 17, the other to GND (with internal pull-up resistor enabled in the code)    |
| GPIO 18 (Pin 24)        | Button (Select/OK)    | Button to confirm the selected PIN value                     | One side of the button to GPIO 18, the other to GND (with internal pull-up resistor enabled in the code)    |
| 3.3V Pin (Pin 36)       | Power                 | Supplies 3.3V to OLED display and LEDs                       | Connect to VCC pins of OLED and LEDs                                                                       |
| GND Pin (Pin 38)        | Ground                | Common ground for the system                                 | Connect to the GND of all components (OLED, buttons, LEDs)                                                 |

## Setup Instructions:

1. **Install MicroPython** on your Raspberry Pi Pico if not already done.
   - Follow the [MicroPython setup guide](https://www.raspberrypi.org/documentation/pico/getting-started/) to install the firmware.
   
2. **Install necessary libraries**:
   - In Thonny, install the **SSD1306** library to interact with the OLED display.
   - Install the **machine** and **time** libraries (both are built-in for MicroPython).

3. **Upload the code**:
   - Clone or download the repository.
   - Open the main Python script (`pin_entry.py`) in Thonny.
   - Upload the script to the Raspberry Pi Pico.

4. **Run the script**:
   - After the script is uploaded, reset the Raspberry Pi Pico.
   - The PIN entry system will initialize and show a masked PIN input screen on the OLED display.

## How It Works:
1. When the system starts, the OLED display shows a prompt to enter a PIN.
2. Press buttons to input digits. The entered digits are displayed as `*` for security.
3. Once the correct PIN is entered, the system will display a success message (green LED flashes).
4. If the incorrect PIN is entered, an error message will appear, and the system will prompt for re-entry (red LED flashes).

## Blog:
For a detailed explanation of how to create this PIN entry system, check out my blog post:  
[Creating a PIN Input System with Raspberry Pi Pico and OLED Display](https://www.ericbzotti.com/creating-a-pin-input-system-with-raspberry-pi-pico-and-oled-display/)

## License:

This project is open-source and licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Author:
Eric B Zotti

## Contributions:
Feel free to fork the repository and submit pull requests if you have any improvements or fixes!
