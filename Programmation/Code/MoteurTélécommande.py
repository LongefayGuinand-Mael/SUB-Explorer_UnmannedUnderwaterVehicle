import RPi.GPIO as GPIO
from collections import Counter
import time
import threading





#####################################################################################
##                      INITIALIZATION : DATA FROM CONTROLLER                      ##
#####################################################################################

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

CH3_LastMainValue = 0
CH6_LastMainValue = 0





######################################################################################
##                        INITIALIZATION : CONTROL OF MOTORS                        ##
######################################################################################

### Initialize all PIN use for the control of the different motors
GPIO.setwarnings(False)
## All steppers
Stepper1 = 27 # CH1-CH4
Stepper2 = 23 # CH1-CH4
Stepper3 = 25 # CH2-CH5
Stepper4 = 6  # CH2-CH5
DirectionStepper1 = 17
DirectionStepper2 = 22
DirectionStepper3 = 24
DirectionStepper4 = 5
GPIO.setup(Stepper1, GPIO.OUT)
GPIO.setup(Stepper2, GPIO.OUT)
GPIO.setup(Stepper3, GPIO.OUT)
GPIO.setup(Stepper4, GPIO.OUT)
GPIO.setup(DirectionStepper1, GPIO.OUT)
GPIO.setup(DirectionStepper2, GPIO.OUT)
GPIO.setup(DirectionStepper3, GPIO.OUT)
GPIO.setup(DirectionStepper4, GPIO.OUT)
## DC Motors
DC_PWM = 13
DC_Direction = 21
GPIO.setup(DC_PWM, GPIO.OUT)
GPIO.setup(DC_Direction,GPIO.OUT)
### Define the frequence for the PWM for the DC Motor
DutyCycle = 0
Hz = 1000
PWM = GPIO.PWM(DC_PWM, Hz)

### Initialize PIN for activate or not the LED Strip
PIN_LED = 18
GPIO.setup(PIN_LED, GPIO.OUT)





######################################################################################
#                      INITIALIZATION : STEPPER MOTOR FUNCTIONS                      #
######################################################################################

### Function create to activate or not the motor turning
def ActivateTurn (CHn_MainValue, pinstep):
    if CHn_MainValue == 1 or CHn_MainValue == -1:
        totalSleep = 0.0005
    if CHn_MainValue == 2 or CHn_MainValue == -2:
        totalSleep = 0.0005
    for x in range(10):
        GPIO.output(pinstep, GPIO.HIGH)
        time.sleep(totalSleep)
        GPIO.output(pinstep, GPIO.LOW)
        time.sleep(totalSleep)
        print("vroom")

### The next 2 functions are defined for the Multi-Threading for Stepper Motors
### Goal here is to turn a number of steps clockwise or anti-clockwise at a given speed
def CoupledMotors1(CHTable_MainValue, Stepper1, DirectionStepper1, Stepper3, DirectionStepper3):
    try :
        # CH1 - Yaw movement (rotation [lacet])
        if CHTable_MainValue[0] == 1 and CHTable_MainValue[3] == 0:
            GPIO.output(DirectionStepper1, GPIO.HIGH) #CW
            ActivateTurn(Stepper1)
        elif CHTable_MainValue[0] == -1 and CHTable_MainValue[3] == 0:
            GPIO.output(DirectionStepper1, GPIO.LOW) #CCW
            ActivateTurn(Stepper1)
        else:
            GPIO.output(Stepper1, GPIO.LOW)

        # CH2 - Pitch movement (rotation [tangage])
        if CHTable_MainValue[1] == 1 and CHTable_MainValue[4] == 0:
            GPIO.output(DirectionStepper3, GPIO.HIGH) #CW
            ActivateTurn(Stepper3)
        elif CHTable_MainValue[1] == -1 and CHTable_MainValue[4] == 0:
            GPIO.output(DirectionStepper3, GPIO.LOW) #CCW
            ActivateTurn(Stepper3)
        else:
            GPIO.output(Stepper3, GPIO.LOW)
        
        # CH4 - Straf movement (translation [latteral])
        if CHTable_MainValue[3] == 1:
            GPIO.output(DirectionStepper1, GPIO.HIGH) #CW
            ActivateTurn(Stepper1)
        elif CHTable_MainValue[3] == -1 :
            GPIO.output(DirectionStepper1, GPIO.LOW) #CCW
            ActivateTurn(Stepper1)
        else:
            GPIO.output(Stepper1, GPIO.LOW)

        # CH5 - Depth movement (translation [profondeur])
        if CHTable_MainValue[4] == 0:
            GPIO.output(Stepper3, GPIO.LOW)
        elif CHTable_MainValue[4] == 1:
            GPIO.output(DirectionStepper3, GPIO.HIGH) #CW
            ActivateTurn(Stepper3)
        elif CHTable_MainValue[4] == -1:
            GPIO.output(DirectionStepper3, GPIO.LOW) #CCW
            ActivateTurn(Stepper3)
        else:
            GPIO.output(Stepper3, GPIO.LOW)

    except AttributeError:
        print('AttributeError : Thread1')

def CoupledMotors2(CHTable_MainValue, Stepper2, DirectionStepper2, Stepper4, DirectionStepper4):
    try : 
        # CH1 - Yaw movement (rotation [lacet])
        if CHTable_MainValue[0] == -1 and CHTable_MainValue[3] == 0:
            GPIO.output(DirectionStepper2, GPIO.LOW) #CW
            ActivateTurn(Stepper2)
        elif CHTable_MainValue[0] == 1 and CHTable_MainValue[3] == 0:
            GPIO.output(DirectionStepper2, GPIO.HIGH) #CCW
            ActivateTurn(Stepper2)
        else:
            GPIO.output(Stepper2, GPIO.LOW)

        # CH2 - Pitch movement (rotation [tangage])
        if CHTable_MainValue[1] == 1 and CHTable_MainValue[4] == 0:
            GPIO.output(DirectionStepper4, GPIO.LOW) #CW
            ActivateTurn(Stepper4)
        elif CHTable_MainValue[1] == -1 and CHTable_MainValue[4] == 0:
            GPIO.output(DirectionStepper4, GPIO.HIGH) #CCW
            ActivateTurn(Stepper4)
        else:
            GPIO.output(Stepper4, GPIO.LOW)
            
        # CH4 - Straf movement (translation [latteral])
        if CHTable_MainValue[3] == -1:
            GPIO.output(DirectionStepper2, GPIO.HIGH) #CW
            ActivateTurn(Stepper2)
        elif CHTable_MainValue[3] == 1:
            GPIO.output(DirectionStepper2, GPIO.LOW) #CCW
            ActivateTurn(Stepper2)
        else:
            GPIO.output(Stepper2, GPIO.LOW)

        # CH5 - Depth movement (translation [profondeur])
        if CHTable_MainValue[4] == 0:
            GPIO.output(Stepper3, GPIO.LOW)
        elif CHTable_MainValue[4] == 1:
            GPIO.output(DirectionStepper4, GPIO.HIGH) #CW
            ActivateTurn(Stepper4)
        elif CHTable_MainValue[4] == -1:
            GPIO.output(DirectionStepper4, GPIO.LOW) #CCW
            ActivateTurn(Stepper4)
        else:
            GPIO.output(Stepper4, GPIO.LOW)

    except AttributeError:
        print('AttributeError : Thread2')





#######################################################################################
##               MAIN PROGRAM : COMMAND ALL MOTORS WITH THE CONTROLLER               ##
#######################################################################################

### Create a loop that will execute this code again and again until the user shutdown the Raspberry Pi
try :
    while True:
        time.sleep(0.02)
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
            if GPIO.input(PIN_CH1) == 0 and CH1_isChecked == False : # CH1
                diff_ch1 = time.time() - t_start
                CH1_isChecked = True
                # Append round diff value in the CH1_LastValues
                if (round(1000000 * diff_ch1 - 1000) < 350) :
                    CH1_LastValues.append(-1)
                if (round(1000000 * diff_ch1 - 1000) >= 350 and round(1000000 * diff_ch1 - 1000) <= 750) :
                    CH1_LastValues.append(0)
                if (round(1000000 * diff_ch1 - 1000) > 750) :
                    CH1_LastValues.append(1)
                CH1_LastValues = CH1_LastValues[-20:]
                # Get the most present value on the CH1_LastValues table
                CH1_MainValue = Counter(CH1_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH2) == 0 and CH2_isChecked == False : # CH2
                diff_ch2 = time.time() - t_start
                CH2_isChecked = True
                if (round(1000000 * diff_ch2 - 1000) < 350) :
                    CH2_LastValues.append(-1)
                if (round(1000000 * diff_ch2 - 1000) >= 350 and round(1000000 * diff_ch2 - 1000) <= 750) :
                    CH2_LastValues.append(0)
                if (round(1000000 * diff_ch2 - 1000) > 750) :
                    CH2_LastValues.append(1)
                CH2_LastValues = CH2_LastValues[-20:]
                # Get the most present value on the CH2_LastValues table
                CH2_MainValue = Counter(CH2_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH3) == 0 and CH3_isChecked == False : # CH3
                diff_ch3 = time.time() - t_start
                CH3_isChecked = True
                # Append round diff value in the CH3_LastValues
                if (round(1000000 * diff_ch3 - 1000) < 350) :
                    CH3_LastValues.append(-1)
                if (round(1000000 * diff_ch3 - 1000) >= 350 and round(1000000 * diff_ch3 - 1000) <= 750) :
                    CH3_LastValues.append(0)
                if (round(1000000 * diff_ch3 - 1000) > 750) :
                    CH3_LastValues.append(1)
                CH3_LastValues = CH3_LastValues[-20:]
                # Get the most present value on the CH3_LastValues table
                CH3_MainValue = Counter(CH3_LastValues).most_common(1)[0][0] 
            if GPIO.input(PIN_CH4) == 0 and CH4_isChecked == False : # CH4
                diff_ch4 = time.time() - t_start
                CH4_isChecked = True
                # Append round diff value in the CH4_LastValues
                if (round(1000000 * diff_ch4 - 1000) < 350) :
                    CH4_LastValues.append(-1)
                if (round(1000000 * diff_ch4 - 1000) >= 350 and round(1000000 * diff_ch4 - 1000) <= 750) :
                    CH4_LastValues.append(0)
                if (round(1000000 * diff_ch4 - 1000) > 750) :
                    CH4_LastValues.append(1)
                CH4_LastValues = CH4_LastValues[-20:]
                # Get the most present value on the CH4_LastValues table
                CH4_MainValue = Counter(CH4_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH5) == 0 and CH5_isChecked == False : # CH5
                diff_ch5 = time.time() - t_start
                CH5_isChecked = True
                # Append round diff value in the CH5_LastValues
                if (round(1000000 * diff_ch5 - 1000) < 350) :
                    CH5_LastValues.append(-1)
                if (round(1000000 * diff_ch5 - 1000) >= 350 and round(1000000 * diff_ch5 - 1000) <= 750) :
                    CH5_LastValues.append(0)
                if (round(1000000 * diff_ch5 - 1000) > 750) :
                    CH5_LastValues.append(1)
                CH5_LastValues = CH5_LastValues[-20:]
                # Get the most present value on the CH5_LastValues table
                CH5_MainValue = Counter(CH5_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH6) == 0 and CH6_isChecked == False : # CH6
                diff_ch6 = time.time() - t_start
                CH6_isChecked = True
                # Append round diff value in the CH6_LastValues
                if (round(1000000 * diff_ch6 - 1000) < 600) :
                    CH6_LastValues.append(0)
                if (round(1000000 * diff_ch6 - 1000) >= 600) :
                    CH6_LastValues.append(1)
                CH6_LastValues = CH6_LastValues[-20:]
                # Get the most present value on the CH6_LastValues table
                CH6_MainValue = Counter(CH6_LastValues).most_common(1)[0][0]
            pass
        
        CHTable_MainValue = [CH1_MainValue, CH2_MainValue, CH3_MainValue, CH4_MainValue, CH5_MainValue, CH6_MainValue]
        print(CHTable_MainValue)
        print('-------------------------------------------')

        ######################################### STRUCTURE #########################################
        ##   ### IF CH3 != 0 -> DC Motors                                                          ##
        ##       ### IF CH3 == 1 or CH3 == -1 -> DC_PWM avec un DutyCycle faible + Gestion sens    ##
        ##       ### IF CH3 == 2 or CH3 == -2 -> DC_PWM avec un DutyCycle fort + Gestion sens      ##
        ##   ### IF CH4 != 0 -> Translation Latterale / Straf                                      ##
        ##   ### IF CH5 != 0 -> Profondeur                                                         ##
        ##   ### IF CH1 != 0 and CH4 == 0 -> Lacet (Rotation)                                      ##
        ##   ### IF CH2 != 0 and CH5 == 0 -> Tangage (Rotation)                                    ##
        ##   ### IF CH6 == 1 -> Allumer LED Strip                                                  ##
        ##       ### ELSE -> Eteindre LED Strip                                                    ##
        #############################################################################################

        Thread1 = threading.Thread(target = CoupledMotors1, args =[CHTable_MainValue, Stepper1, DirectionStepper1, Stepper3, DirectionStepper3])
        Thread2 = threading.Thread(target = CoupledMotors2, args =[CHTable_MainValue, Stepper2, DirectionStepper2, Stepper4, DirectionStepper4])
        Thread1.start()
        Thread2.start()

        # DC Motor --> CH3
        if CH3_MainValue != CH3_LastMainValue:
            if CH3_MainValue == 0: # DC Motor : Stop movement
                GPIO.output(DC_PWM,GPIO.LOW)
                GPIO.output(DC_Direction,GPIO.LOW)
                PWM.stop()
            else:
                if CH3_MainValue == 1 or CH3_MainValue == -1: # Define DutyClycle for DC Motor
                    DutyCycle = 35
                elif CH3_MainValue == 2 or CH3_MainValue == -2: # Define DutyClycle for DC Motor
                    DutyCycle = 95
                if CH3_MainValue > 0 : # DC Motor : Frontward movement
                    GPIO.output(DC_Direction,GPIO.HIGH)
                    PWM.start(DutyCycle)
                elif CH3_MainValue < 0: # DC Motor : Backward movement
                    GPIO.output(DC_Direction,GPIO.LOW)
                    PWM.start(DutyCycle)
                else: # DC Motor : Stop movement // Just for secure
                    GPIO.output(DC_PWM,GPIO.LOW)
                    GPIO.output(DC_Direction,GPIO.LOW)
                    PWM.stop()
            CH3_LastMainValue = CH3_MainValue
        
        # LED Strip --> CH6
        if CH6_MainValue != CH6_LastMainValue:
            if CH6_MainValue == 0: # Light OFF the LED Strip
                GPIO.output(PIN_LED,GPIO.LOW)
            if CH6_MainValue == 1: # Light ON the LED Strip
                GPIO.output(PIN_LED, GPIO.HIGH)



finally : 
    GPIO.cleanup()

