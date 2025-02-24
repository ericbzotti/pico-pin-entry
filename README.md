# MicroPython-based PIN Entry System

This project is a PIN entry system built using a Raspberry Pi Pico, MicroPython, and an OLED display. It allows secure PIN input using push buttons, providing a simple yet effective security mechanism for any project requiring user authentication.

## Components Used:
- **Raspberry Pi Pico**: A microcontroller with sufficient GPIO pins for input and display.
- **OLED Display (128x64)**: To display the PIN input and status.
- **Push Buttons**: Used for entering the PIN.
- **MicroPython**: The software framework for controlling the Raspberry Pi Pico.

## Features:
- Secure PIN entry using push buttons.
- OLED display shows the entered PIN (masked) and feedback messages.
- Simple yet effective for any small security-based project.

## Requirements:
1. **Hardware**:
   - Raspberry Pi Pico
   - OLED display (128x64 SSD1306)
   - 4 push buttons (for each digit and navigation)
   - Jumper wires and breadboard for connections

2. **Software**:
   - [MicroPython](https://micropython.org/download/rp2-pico/) installed on Raspberry Pi Pico
   - [Thonny IDE](https://thonny.org/) for writing and deploying MicroPython code

## Wiring:

| Raspberry Pi Pico Pin | OLED Display Pin | Push Button Pin |
|-----------------------|------------------|-----------------|
| GP0                   | SCL              | Button 1        |
| GP1                   | SDA              | Button 2        |
| 3V3                   | VCC              | Button 3        |
| GND                   | GND              | Button 4        |

- Connect the OLED display via I2C (SCL to GP0, SDA to GP1).
- Connect the push buttons to the appropriate GPIO pins.

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
3. Once the correct PIN is entered, the system will display a success message.
4. If the incorrect PIN is entered, an error message will appear, and the system will prompt for re-entry.

## License:

This project is open-source and licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Author:
Eric B Zotti
