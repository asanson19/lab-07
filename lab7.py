import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)


#set output
GPIO.output(11, 1)


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


#set inputs
light_sensor = 21
sound_sensor = 21
GPIO.setup(light_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sound_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




#LED ON & OFF
pwm = 11
def on_led_fun():
   pwm.start(50)




def off_led_fun():
   pwm.stop()




#for led blinking
def b_LED(num_b, on_led, off_led):
   for i in range(num_b):
       on_led_fun()
       time.sleep(on_led)
       off_led_fun()
       time.sleep(off_led)




#for light input
light_treshold = 300
def input_light():
    return GPIO.input(sound_sensor)




def read_light():
    val_light = input_light()
    if val_light > light_treshold:
        print("BRIGHT")
    else:
        print("DARK")
    return val_light


#for sound input
sound_treshold = 150
def input_sound():
    return GPIO.input(light_sensor)




def read_sound():
    val_sound = input_sound()
    if val_sound > sound_treshold:
        on_led_fun()
        time.sleep(0.1)
        off_led_fun()
    print("SOUND VAL:", val_sound)
    return val_sound




#PWM LED
pwm = GPIO.PWM(11, 1000)




#Loop
while True:
   b_LED(5, 0.5,0.5)




   count = time.time()
   while time.time() - count < 5:
       read_light()
       time.sleep(0.1)




   b_LED(4, 0.2, 0.2)




   count_2 = time.time()
   while time.time() - count_2 < 5:
       read_sound()
       time.sleep(0.1)







