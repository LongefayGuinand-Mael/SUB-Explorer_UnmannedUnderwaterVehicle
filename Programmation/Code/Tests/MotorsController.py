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

CHTable_LastMainValue = [0]*6
CH1_LastMainValue = 0
CH2_LastMainValue = 0
CH3_LastMainValue = 0
CH4_LastMainValue = 0
CH5_LastMainValue = 0
CH6_LastMainValue = 0





######################################################################################
##                        INITIALIZATION : CONTROL OF MOTORS                        ##
######################################################################################

### Initialize all PIN use for the control of the different motors
GPIO.setwarnings(False)
## All steppers
Stepper1 = 27                   # CH4+CH1 -> Straf and Yaw movements
Stepper2 = 23                   # CH4+CH1 -> Straf and Yaw movements
Stepper3 = 25                   # CH5+CH2 -> Depth and Pitch movements
Stepper4 = 6                    # CH5+CH2 -> Depth and Pitch movements
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
### Define the frequence and the duty-cycle for the PWM for the DC Motor
DutyCycle = 85
Hz = 1000
PWM = GPIO.PWM(DC_PWM, Hz)

### Initialize PIN for activate or not the LED Strip
PIN_LED = 18
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.output(PIN_LED, GPIO.HIGH) # This line is here because we have a little problem with CH6. When CH6_MainValue=1, there are some interferences disturbance with the 5 other receptor channels





######################################################################################
##                     INITIALIZATION : STEPPER MOTOR FUNCTIONS                     ##
######################################################################################

### Function create to activate the selected motor with the right
def ActivateTurn (CHn_MainValue, pinstep):
    if CHn_MainValue == 1 or CHn_MainValue == -1:
        totalSleep = 0.00005
    if CHn_MainValue == 2 or CHn_MainValue == -2:
        totalSleep = 0.0000025
    GPIO.output(pinstep, GPIO.HIGH)
    GPIO.output(pinstep, GPIO.LOW)
    time.sleep(totalSleep)

### Function create to stop the selected motor
#def StopTurn (pinstep):
#    GPIO.output(pinstep, GPIO.LOW)

### The next 2 functions are defined for the Multi-Threading for Stepper Motors
### Goal here is to turn a number of steps clockwise or anti-clockwise at a given speed
def CoupledMotors1(CHTable_MainValue, CHTable_LastMainValue, Stepper1, DirectionStepper1, Stepper3, DirectionStepper3):
    try :
        if CHTable_MainValue[0] != CHTable_LastMainValue[0]:
            # CH1 - Yaw movement (rotation [lacet])
            if CHTable_MainValue[0] > 0 and CHTable_MainValue[3] == 0:
                GPIO.output(DirectionStepper1, GPIO.HIGH) #CW
                ActivateTurn(CHTable_MainValue[0], Stepper1)
            elif CHTable_MainValue[0] < 0 and CHTable_MainValue[3] == 0:
                GPIO.output(DirectionStepper1, GPIO.LOW) #CCW
                ActivateTurn(CHTable_MainValue[0], Stepper1)
        
        if CHTable_MainValue[1] != CHTable_LastMainValue[1]:
            # CH2 - Pitch movement (rotation [tangage])
            if CHTable_MainValue[1] > 0 and CHTable_MainValue[4] == 0:
                GPIO.output(DirectionStepper3, GPIO.HIGH) #CW
                ActivateTurn(CHTable_MainValue[1], Stepper3)
            elif CHTable_MainValue[1] < 0 and CHTable_MainValue[4] == 0:
                GPIO.output(DirectionStepper3, GPIO.LOW) #CCW
                ActivateTurn(CHTable_MainValue[1], Stepper3)
        
        if CHTable_MainValue[3] != CHTable_LastMainValue[3]:
            # CH4 - Straf movement (translation [latteral])
            if CHTable_MainValue[3] > 0:
                GPIO.output(DirectionStepper1, GPIO.HIGH) #CW
                ActivateTurn(CHTable_MainValue[3], Stepper1)
            elif CHTable_MainValue[3] < 0:
                GPIO.output(DirectionStepper1, GPIO.LOW) #CCW
                ActivateTurn(CHTable_MainValue[3], Stepper1)

        if CHTable_MainValue[4] != CHTable_LastMainValue[4]:
            # CH5 - Depth movement (translation [profondeur])
            if CHTable_MainValue[4] > 0:
                GPIO.output(DirectionStepper3, GPIO.HIGH) #CW
                ActivateTurn(CHTable_MainValue[4], Stepper3)
            elif CHTable_MainValue[4] < 0:
                GPIO.output(DirectionStepper3, GPIO.LOW) #CCW
                ActivateTurn(CHTable_MainValue[4], Stepper3)

    except AttributeError:
        print('AttributeError : Thread1')

def CoupledMotors2(CHTable_MainValue, CHTable_LastMainValue, Stepper2, DirectionStepper2, Stepper4, DirectionStepper4):
    try : 
        if CHTable_MainValue[0] != CHTable_LastMainValue[0]:
            # CH1 - Yaw movement (rotation [lacet])
            if CHTable_MainValue[0] < 0 and CHTable_MainValue[3] == 0:
                GPIO.output(DirectionStepper2, GPIO.LOW) #CW
                ActivateTurn(CHTable_MainValue[0], Stepper2)
            elif CHTable_MainValue[0] > 0 and CHTable_MainValue[3] == 0:
                GPIO.output(DirectionStepper2, GPIO.HIGH) #CCW
                ActivateTurn(CHTable_MainValue[0], Stepper2)

        if CHTable_MainValue[1] != CHTable_LastMainValue[1]:
            # CH2 - Pitch movement (rotation [tangage])
            if CHTable_MainValue[1] > 0 and CHTable_MainValue[4] == 0:
                GPIO.output(DirectionStepper4, GPIO.LOW) #CW
                ActivateTurn(CHTable_MainValue[1], Stepper4)
            elif CHTable_MainValue[1] < 0 and CHTable_MainValue[4] == 0:
                GPIO.output(DirectionStepper4, GPIO.HIGH) #CCW
                ActivateTurn(CHTable_MainValue[1], Stepper4)
            
        if CHTable_MainValue[3] != CHTable_LastMainValue[3]:
            # CH4 - Straf movement (translation [latteral])
            if CHTable_MainValue[3] < 0:
                GPIO.output(DirectionStepper2, GPIO.HIGH) #CW
                ActivateTurn(CHTable_MainValue[3], Stepper2)
            elif CHTable_MainValue[3] > 0:
                GPIO.output(DirectionStepper2, GPIO.LOW) #CCW
                ActivateTurn(CHTable_MainValue[3], Stepper2)

        if CHTable_MainValue[4] != CHTable_LastMainValue[4]:
            # CH5 - Depth movement (translation [profondeur])
            if CHTable_MainValue[4] > 0:
                GPIO.output(DirectionStepper4, GPIO.HIGH) #CW
                ActivateTurn(CHTable_MainValue[4], Stepper4)
            elif CHTable_MainValue[4] < 0:
                GPIO.output(DirectionStepper4, GPIO.LOW) #CCW
                ActivateTurn(CHTable_MainValue[4], Stepper4)

    except AttributeError:
        print('AttributeError : Thread2')





#######################################################################################
##               MAIN PROGRAM : COMMAND ALL MOTORS WITH THE CONTROLLER               ##
#######################################################################################

### Create a loop that will execute this code again and again until the user shutdown the Raspberry Pi
try :
    LoopCounter = 0
    while True:
        LoopCounter += 1
        #time.sleep(0.02)

        while (GPIO.input(PIN_CH1) == 0 and GPIO.input(PIN_CH2) == 0 and GPIO.input(PIN_CH3) == 0 and GPIO.input(PIN_CH4) == 0 and GPIO.input(PIN_CH5) == 0 and GPIO.input(PIN_CH6) == 0) :
            pass
        t_start = time.time()
        CH1_isChecked = False
        CH2_isChecked = False
        CH3_isChecked = False
        CH4_isChecked = False
        CH5_isChecked = False
        CH6_isChecked = True # Set up to TRUE because of the problem on CH6
        
        ### Create a table to control all motors with the 2.4GHz controller
        while (time.time() < t_start + 0.02) :
            if GPIO.input(PIN_CH1) == 0 and CH1_isChecked == False : # CH1
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
            if GPIO.input(PIN_CH2) == 0 and CH2_isChecked == False : # CH2
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
            if GPIO.input(PIN_CH3) == 0 and CH3_isChecked == False : # CH3
                diff_ch3 = time.time() - t_start
                CH3_isChecked = True
                # Append round diff value in the CH3_LastValues
                if (round(1000000 * diff_ch3 - 1000) < 250) :
                    CH3_LastValues.append(-2)
                if (round(1000000 * diff_ch3 - 1000) >= 250 and round(1000000 * diff_ch3 - 1000) < 400) :
                    CH3_LastValues.append(-1)
                if (round(1000000 * diff_ch3 - 1000) >= 400 and round(1000000 * diff_ch3 - 1000) < 650) :
                    CH3_LastValues.append(0)
                if (round(1000000 * diff_ch3 - 1000) >= 650 and round(1000000 * diff_ch3 - 1000) < 800) :
                    CH3_LastValues.append(1)
                if (round(1000000 * diff_ch3 - 1000) > 800) :
                    CH3_LastValues.append(2)
                CH3_LastValues = CH3_LastValues[-20:]
                # Get the most present value on the CH3_LastValues table
                CH3_MainValue = Counter(CH3_LastValues).most_common(1)[0][0] 
            if GPIO.input(PIN_CH4) == 0 and CH4_isChecked == False : # CH4
                diff_ch4 = time.time() - t_start
                CH4_isChecked = True
                # Append round diff value in the CH4_LastValues
                if (round(1000000 * diff_ch4 - 1000) < 200) :
                    CH4_LastValues.append(-2)
                if (round(1000000 * diff_ch4 - 1000) >= 200 and round(1000000 * diff_ch4 - 1000) < 400) :
                    CH4_LastValues.append(-1)
                if (round(1000000 * diff_ch4 - 1000) >= 400 and round(1000000 * diff_ch4 - 1000) < 650) :
                    CH4_LastValues.append(0)
                if (round(1000000 * diff_ch4 - 1000) >= 650 and round(1000000 * diff_ch4 - 1000) < 800) :
                    CH4_LastValues.append(1)
                if (round(1000000 * diff_ch4 - 1000) > 800) :
                    CH4_LastValues.append(2)
                CH4_LastValues = CH4_LastValues[-20:]
                # Get the most present value on the CH4_LastValues table
                CH4_MainValue = Counter(CH4_LastValues).most_common(1)[0][0]
            if GPIO.input(PIN_CH5) == 0 and CH5_isChecked == False : # CH5
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
#            if GPIO.input(PIN_CH6) == 0 and CH6_isChecked == False : # CH6
#                diff_ch6 = time.time() - t_start
#                CH6_isChecked = True
#                # Append round diff value in the CH6_LastValues
#                if (round(1000000 * diff_ch6 - 1000) < 500) :
#                    CH6_LastValues.append(0)
#                if (round(1000000 * diff_ch6 - 1000) >= 500) :
#                    CH6_LastValues.append(1)
#                CH6_LastValues = CH6_LastValues[-20:]
#                # Get the most present value on the CH6_LastValues table
#                CH6_MainValue = Counter(CH6_LastValues).most_common(1)[0][0]
            pass
        
        CHTable_MainValue = [CH1_MainValue, CH2_MainValue, CH3_MainValue, CH4_MainValue, CH5_MainValue, CH6_MainValue]
#        CHTable_MainValue = [CH1_MainValue, CH2_MainValue, CH3_MainValue, CH4_MainValue, CH5_MainValue]
        print(CHTable_MainValue)
        print('-------------------------------------------')

        ########################################## STRUCTURE ##########################################
        ##   ### IF CH3 != 0 -> DC Motors                                                            ##
        ##       ### IF CH3 == 1 or CH3 == -1 -> DC_PWM with a low DutyCycle + Direction gestion     ##
        ##       ### IF CH3 == 2 or CH3 == -2 -> DC_PWM with a high DutyCycle + Direction gestion    ##
        ##   ### IF CH4 != 0 -> Straf movement [Translation Latterale]                               ##
        ##   ### IF CH5 != 0 -> Depth movement [Translation Profondeur]                              ##
        ##   ### IF CH1 != 0 and CH4 == 0 -> Yaw movement [Lacet (Rotation)]                         ##
        ##   ### IF CH2 != 0 and CH5 == 0 -> Pitch movement [Tangage (Rotation)]                     ##
        ##   ### IF CH6 == 1 -> Light ON the LED Strip                                               ##
        ##       ### ELSE -> Light OFF the LED Strip                                                 ##
        ###############################################################################################
        
        if LoopCounter % 10 == 0:
            CHTable_LastMainValue = CHTable_MainValue
            # All Stepper Motors --> CH1-CH2-CH4-CH5
            Thread1 = threading.Thread(target = CoupledMotors1, args =[CHTable_MainValue, CHTable_LastMainValue, Stepper1, DirectionStepper1, Stepper3, DirectionStepper3])
            Thread2 = threading.Thread(target = CoupledMotors2, args =[CHTable_MainValue, CHTable_LastMainValue, Stepper2, DirectionStepper2, Stepper4, DirectionStepper4])
            Thread1.start()
            Thread2.start()

        # DC Motor --> CH3
        if CH3_MainValue != CH3_LastMainValue:
            if CH3_MainValue == 0: # DC Motor : Stop movement
                GPIO.output(DC_PWM,GPIO.LOW)
                GPIO.output(DC_Direction,GPIO.LOW)
                PWM.stop()
            else:
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
        
#        # LED Strip --> CH6
#        if CH6_MainValue != CH6_LastMainValue:
#            if CH6_MainValue == 0: # Light OFF the LED Strip
#                GPIO.output(PIN_LED,GPIO.LOW)
#            if CH6_MainValue == 1: # Light ON the LED Strip
#                GPIO.output(PIN_LED, GPIO.HIGH)



finally : 
    GPIO.cleanup()