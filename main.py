from machine import Pin, I2C
import ssd1306
import time
import random

# Initialize I2C and OLED display
# i2c = I2C(0, scl=Pin(5), sda=Pin(4))
i2c = I2C(1, scl=Pin(15), sda=Pin(14))

led_green = Pin(13, Pin.OUT)
led_red = Pin(12, Pin.OUT)

#error message
error_message = ""

# Initialize OLED display
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialisation des broches des boutons
button_up = Pin(16, Pin.IN, Pin.PULL_UP)  # Bouton pour augmenter le chiffre
button_down = Pin(17, Pin.IN, Pin.PULL_UP)  # Bouton pour diminuer le chiffre
button_select = Pin(18, Pin.IN, Pin.PULL_UP)  # Bouton pour diminuer le chiffre

def flash_green():
    global error_message  # Use the global variable to store the error message
    error_message=""
    led_green.value(1)  # Turn green LED on
    time.sleep(.2)
    led_green.value(0)  # Turn green LED off
    
def flash_red(err_message):
    global error_message  # Use the global variable to store the error message
    error_message=err_message
    print(error_message)  # Display the error message
    led_red.value(1)  # Turn red LED on
    time.sleep(.1)
    led_red.value(0)  # Turn red LED off


def enter_pin():
    display.fill(0)
    code_completed = 0
    pin = []
    curseurPosition = random.randint(0, 9) + 1
    curseurValues = ['del',0 , 1, 2, 3, 4, 5, 6 , 7, 8, 9, 'ok'] 
    curseurDisplay = [ '__',
                   '   _',
                   '    _',
                   '     _',
                   '      _',
                   '       _',
                   '        _',
                   '         _',
                   '          _',
                   '           _',
                   '            _',
                   '              __']

    current_digit = 1

    while code_completed==0:  # Limite à 8 chiffres
        if not button_up.value():
            display.fill(0)
            curseurPosition=curseurPosition-1
            if curseurPosition == -1:
                curseurPosition = 11
            time.sleep(0.2)  # Anti-rebond
            flash_green()
        elif not button_down.value():
            display.fill(0)
            curseurPosition=curseurPosition+1
            if curseurPosition == 12:
                curseurPosition = 0
            time.sleep(0.2)  # Anti-rebond
            flash_green()
        elif not button_select.value():
            display.fill(0)
            if curseurPosition == 0 and len(pin) > 0:
                pin.pop()
                time.sleep(0.2)  # Anti-rebon
                flash_green()
            elif curseurPosition == 0 and len(pin) == 0:
                flash_red("PIN is empty")
            elif curseurPosition == 11 and len(pin) >= 4 and len(pin) <= 8:
                time.sleep(0.2)  # Anti-rebon
                flash_green();
                code_completed=1;
            elif curseurPosition == 11 and len(pin) < 4:
                time.sleep(0.2)  # Anti-rebon
                flash_red("min 4 numbers")                
            elif len(pin) < 8:
                pin.append(curseurValues[curseurPosition])
                curseurPosition = random.randint(0, 9) + 1
                time.sleep(0.2)  # Anti-rebon
                flash_green()
            else:
                flash_red("max 8 numbers")
        # Affichage du code PIN actuel (par exemple, sur un écran OLED)
        display.text('Choose a PIN', 0, 0)
        display.text("<- 0123456789 OK", 0, 10)
        display.text(curseurDisplay[curseurPosition],0 , 14)
        display.text(''.join(map(str, pin)), 0, 30)
        display.text(error_message, 0, 55)
        display.show()
        time.sleep(0.1)

    return ''.join(map(str, pin))

pin = enter_pin()
print(pin)
