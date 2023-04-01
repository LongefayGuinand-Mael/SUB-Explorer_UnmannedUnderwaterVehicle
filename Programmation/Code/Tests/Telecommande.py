import RPi.GPIO as GPIO
from collections import Counter
import time

### Initialize all PIN use for get datas from 2.4GHz controller
PIN_CH1 = 12
PIN_CH2 = 19
PIN_CH3 = 16
PIN_CH4 = 26
PIN_CH5 = 20
PIN_CH6 = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_CH1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_CH2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_CH3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_CH4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_CH5, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_CH6, GPIO.IN, pull_up_down = GPIO.PUD_UP)

### Initialize lists for 10 last values of each get datas
CH1_LastValues = [0]*20
CH2_LastValues = [0]*20
CH3_LastValues = [0]*20
CH4_LastValues = [0]*20
CH5_LastValues = [0]*20
CH6_LastValues = [0]*20

### Initialize main values for the future code (for motors)
CHTable_MainValue = [0]*6
CH1_MainValue = 0
CH2_MainValue = 0
CH3_MainValue = 0
CH4_MainValue = 0
CH5_MainValue = 0
CH6_MainValue = 0

try :
    while True:
        #time.sleep(0.02)
        
        while (GPIO.input(PIN_CH1) == 0 and GPIO.input(PIN_CH2) == 0 and GPIO.input(PIN_CH3) == 0 and GPIO.input(PIN_CH4) == 0 and GPIO.input(PIN_CH5) == 0 and GPIO.input(PIN_CH6) == 0) :
            pass
        t_start = time.time()
        CH1_isChecked = False
        CH2_isChecked = False
        CH3_isChecked = False
        CH4_isChecked = False
        CH5_isChecked = False
        CH6_isChecked = False
        
        ### Create a table to control all motors with the 2.4GHz controller
        while (time.time() < t_start + 0.02) :
            if GPIO.input(PIN_CH1) == 0 and CH1_isChecked == False :
                diff_ch1 = time.time() - t_start
                CH1_isChecked = True
                # Append round diff value in the CH1_LastValues
                if (round(1000000 * diff_ch1 - 1000) < 250) :
                    CH1_LastValues.append(-2)
                if (round(1000000 * diff_ch1 - 1000) >= 250 and round(1000000 * diff_ch1 - 1000) < 415) :
                    CH1_LastValues.append(-1)
                if (round(1000000 * diff_ch1 - 1000) >= 415 and round(1000000 * diff_ch1 - 1000) < 585) :
                    CH1_LastValues.append(0)
                if (round(1000000 * diff_ch1 - 1000) >= 585 and round(1000000 * diff_ch1 - 1000) < 750) :
                    CH1_LastValues.append(1)
                if (round(1000000 * diff_ch1 - 1000) > 750) :
                    CH1_LastValues.append(2)
                CH1_LastValues = CH1_LastValues[-20:]
                # Get the most present value on the CH1_LastValues table
                CH1_MainValue = Counter(CH1_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH2) == 0 and CH2_isChecked == False :
                diff_ch2 = time.time() - t_start
                CH2_isChecked = True
                if (round(1000000 * diff_ch2 - 1000) < 250) :
                    CH2_LastValues.append(-2)
                if (round(1000000 * diff_ch2 - 1000) >= 250 and round(1000000 * diff_ch2 - 1000) < 415) :
                    CH2_LastValues.append(-1)
                if (round(1000000 * diff_ch2 - 1000) >= 415 and round(1000000 * diff_ch2 - 1000) < 585) :
                    CH2_LastValues.append(0)
                if (round(1000000 * diff_ch2 - 1000) >= 585 and round(1000000 * diff_ch2 - 1000) < 750) :
                    CH2_LastValues.append(1)
                if (round(1000000 * diff_ch2 - 1000) > 750) :
                    CH2_LastValues.append(2)
                CH2_LastValues = CH2_LastValues[-20:]
                # Get the most present value on the CH2_LastValues table
                CH2_MainValue = Counter(CH2_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH3) == 0 and CH3_isChecked == False :
                diff_ch3 = time.time() - t_start
                CH3_isChecked = True
                # Append round diff value in the CH3_LastValues
                if (round(1000000 * diff_ch3 - 1000) < 250) :
                    CH3_LastValues.append(-2)
                if (round(1000000 * diff_ch3 - 1000) >= 250 and round(1000000 * diff_ch3 - 1000) < 435) :
                    CH3_LastValues.append(-1)
                if (round(1000000 * diff_ch3 - 1000) >= 435 and round(1000000 * diff_ch3 - 1000) < 565) :
                    CH3_LastValues.append(0)
                if (round(1000000 * diff_ch3 - 1000) >= 565 and round(1000000 * diff_ch3 - 1000) < 750) :
                    CH3_LastValues.append(1)
                if (round(1000000 * diff_ch3 - 1000) > 750) :
                    CH3_LastValues.append(2)
                CH3_LastValues = CH3_LastValues[-20:]
                # Get the most present value on the CH3_LastValues table
                CH3_MainValue = Counter(CH3_LastValues).most_common(1)[0][0] 
            if GPIO.input(PIN_CH4) == 0 and CH4_isChecked == False :
                diff_ch4 = time.time() - t_start
                CH4_isChecked = True
                # Append round diff value in the CH4_LastValues
                if (round(1000000 * diff_ch4 - 1000) < 250) :
                    CH4_LastValues.append(-2)
                if (round(1000000 * diff_ch4 - 1000) >= 250 and round(1000000 * diff_ch4 - 1000) < 435) :
                    CH4_LastValues.append(-1)
                if (round(1000000 * diff_ch4 - 1000) >= 435 and round(1000000 * diff_ch4 - 1000) < 565) :
                    CH4_LastValues.append(0)
                if (round(1000000 * diff_ch4 - 1000) >= 565 and round(1000000 * diff_ch4 - 1000) < 750) :
                    CH4_LastValues.append(1)
                if (round(1000000 * diff_ch4 - 1000) > 750) :
                    CH4_LastValues.append(2)
                CH4_LastValues = CH4_LastValues[-20:]
                # Get the most present value on the CH4_LastValues table
                CH4_MainValue = Counter(CH4_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH5) == 0 and CH5_isChecked == False :
                diff_ch5 = time.time() - t_start
                CH5_isChecked = True
                # Append round diff value in the CH5_LastValues
                if (round(1000000 * diff_ch5 - 1000) < 250) :
                    CH5_LastValues.append(-2)
                if (round(1000000 * diff_ch5 - 1000) >= 250 and round(1000000 * diff_ch5 - 1000) < 435) :
                    CH5_LastValues.append(-1)
                if (round(1000000 * diff_ch5 - 1000) >= 435 and round(1000000 * diff_ch5 - 1000) < 565) :
                    CH5_LastValues.append(0)
                if (round(1000000 * diff_ch5 - 1000) >= 565 and round(1000000 * diff_ch5 - 1000) < 750) :
                    CH5_LastValues.append(1)
                if (round(1000000 * diff_ch5 - 1000) > 750) :
                    CH5_LastValues.append(2)
                CH5_LastValues = CH5_LastValues[-20:]
                # Get the most present value on the CH5_LastValues table
                CH5_MainValue = Counter(CH5_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH6) == 0 and CH6_isChecked == False :
                diff_ch6 = time.time() - t_start
                CH6_isChecked = True
                # Append round diff value in the CH6_LastValues
                if (round(1000000 * diff_ch6 - 1000) < 500) :
                    CH6_LastValues.append(0)
                if (round(1000000 * diff_ch6 - 1000) >= 500) :
                    CH6_LastValues.append(1)
                CH6_LastValues = CH6_LastValues[-20:]
                # Get the most present value on the CH6_LastValues table
                CH6_MainValue = Counter(CH6_LastValues).most_common(1)[0][0]
            pass
        
        CHTable_MainValue = [CH1_MainValue, CH2_MainValue, CH3_MainValue, CH4_MainValue, CH5_MainValue, CH6_MainValue]

        #print("CH1: ", CH1_MainValue, "  | CH2: ", CH2_MainValue, "  | CH3: ", CH3_MainValue, "  | CH4: ", CH4_MainValue, "  | CH5: ", CH5_MainValue, "  | CH6: ", CH6_MainValue)
        print(CHTable_MainValue)
        
finally : 
    GPIO.cleanup()



