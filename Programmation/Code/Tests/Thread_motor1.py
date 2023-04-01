# Pour executer le prog. en ligne de commande  
from curses.ascii import DC1
from turtle import up
from pynput import keyboard     # Bibliotheque de gestion clavier
from time import sleep          # Bibliotheque de gestion du temps
import RPi.GPIO as GPIO         # Bibliotheque de gestion des GPIO 
import threading

# Moteur stepper 
STEP_1 = 14                     # La commande d'avance d'un pas est connectee -> GPIO14  
DIR_1 = 15                      # La commande du sens de rotation est connectee -> GPIO15
STEP_2 = 23                      
DIR_2= 24
STEP_3 = 17                     # Moteurs profondeur / tangage
DIR_3 = 27
STEP_4 = 5
DIR_4 = 6
# Moteur dc
DC_PWM = 13
DC_DIR1 = 16
DC_DIR2 = 20 

# Moteur stepper  
GPIO.setmode(GPIO.BCM)                  # Utiliser la numerotation BCM pour les GPIO
GPIO.setwarnings(False)                 # Ne pas afficher les alertes
GPIO.setup(STEP_1, GPIO.OUT)            # Parametrer GPIO14 en sortie
GPIO.setup(DIR_1, GPIO.OUT)             # Parametrer GPIO15 en sortie
GPIO.setup(STEP_2, GPIO.OUT)     
GPIO.setup(DIR_2, GPIO.OUT)    
GPIO.setup(STEP_3, GPIO.OUT)     
GPIO.setup(DIR_3, GPIO.OUT)
GPIO.setup(STEP_4, GPIO.OUT)     
GPIO.setup(DIR_4, GPIO.OUT)
# Moteur dc
GPIO.setup(DC_PWM, GPIO.OUT)
GPIO.setup(DC_DIR1,GPIO.OUT)
GPIO.setup(DC_DIR1,GPIO.OUT)
dc = 25 #duty cycle [0-100]
hz = 1000 #frequence
pwm = GPIO.PWM(DC_PWM,hz)

# Tourner d'un nombre de pas en CW ou CCW a une vitesse donnee
def tourne1(entree,pindir1,pinstep1,pindir2,pinstep2):
    
    # Avancer du nombre de pas
    def vroom (pinstep):
        for x in range(10):
            GPIO.output(pinstep, GPIO.HIGH)
            sleep(0.0005)
            GPIO.output(pinstep, GPIO.LOW)
            sleep(0.0005)
    try :

        # Sens de rotation/moteurlat_1
        #straf
        if entree == "Key.left":
            GPIO.output(pindir1, GPIO.HIGH) #CW
            vroom(pinstep1)
        elif entree == "Key.right":
            GPIO.output(pindir1, GPIO.LOW) #CCW
            vroom(pinstep1)

        # Sens de rotation/moteurhori_1
        #profondeur
        elif entree == "Key.up":
            GPIO.output(pindir2, GPIO.HIGH) #CW
            vroom(pinstep2)
        elif entree == "Key.down":
            GPIO.output(pindir2, GPIO.LOW) #CCW
            vroom(pinstep2)


        # Sens de rotation/moteurlat_1
        #lacet
        if entree == "q":
            GPIO.output(pindir1, GPIO.HIGH) #CW
            vroom(pinstep1)
        elif entree == "d":
            GPIO.output(pindir1, GPIO.LOW) #CCW
            vroom(pinstep1)


        # Sens de rotation/moteurhori_1
        #tanguage
        if entree == "z":
            GPIO.output(pindir2, GPIO.HIGH) #CW
            vroom(pinstep2)
        elif entree == "s":
            GPIO.output(pindir2, GPIO.LOW) #CCW
            vroom(pinstep2)

    except AttributeError:
        print('Touche speciale : {0}'.format(key))

def tourne2(entree,pindir1,pinstep1,pindir2,pinstep2):
    
    # Avancer du nombre de pas
    def vroom (pinstep):
        for x in range(10):
            GPIO.output(pinstep, GPIO.HIGH)
            sleep(0.0005)
            GPIO.output(pinstep, GPIO.LOW)
            sleep(0.0005)
    try : 

    # Sens de rotation/moteurlat_1
    #straf
        if entree == "Key.left":
            GPIO.output(pindir1, GPIO.HIGH) #CW
            vroom(pinstep1)
        elif entree == "Key.right":
            GPIO.output(pindir1, GPIO.LOW) #CCW
            vroom(pinstep1)

        # Sens de rotation/moteurhori_1
        #profondeur
        elif entree == "Key.up":
            GPIO.output(pindir2, GPIO.HIGH) #CW
            vroom(pinstep2)
        elif entree == "Key.down":
            GPIO.output(pindir2, GPIO.LOW) #CCW
            vroom(pinstep2)

        # Sens de rotation/moteurlat_1
        #lacet
        elif entree == "q":
            GPIO.output(pindir1, GPIO.LOW) #CW
            vroom(pinstep1)
        elif entree == "d":
            GPIO.output(pindir1, GPIO.HIGH) #CCW
            vroom(pinstep1)


        # Sens de rotation/moteurhori_1
        #tanguage
        if entree == "z":
            GPIO.output(pindir2, GPIO.LOW) #CW
            vroom(pinstep2)
        elif entree == "s":
            GPIO.output(pindir2, GPIO.HIGH) #CCW
            vroom(pinstep2)

    except AttributeError:
        print('Touche speciale : {0}'.format(key))
                
# Fonction appelee quand une touche est appuyee
def appui(key):
    try:
        entree = format(key.char)
        print('Touche alphanumerique : {0} '.format(key.char))
        t1 = threading.Thread(target = tourne1, args =[entree,15,14,27,17])
        t2 = threading.Thread(target = tourne2, args =[entree,24,23,6,5])
        t1.start()
        t2.start()
        #moteur dc
        if entree =="e":
            GPIO.output(DC_DIR1,GPIO.HIGH)
            GPIO.output(DC_DIR2,GPIO.LOW)
            pwm.start(dc)
            sleep(0.3)
            pwm.stop()
        elif entree == "a":
            GPIO.output(DC_DIR1,GPIO.LOW)
            GPIO.output(DC_DIR2,GPIO.HIGH)
            pwm.start(dc)
            sleep(0.3)
            pwm.stop()

    except AttributeError:
        entree = format(key)
        print('Touche speciale : {0}'.format(key))
        t1 = threading.Thread(target = tourne1, args =[entree,15,14,27,17])
        t2 = threading.Thread(target = tourne2, args =[entree,24,23,6,5])
        t1.start()
        t2.start()
  
           
# Fonction executee quand une touche est relachee
def relache(key):
    print('Key released: {0}'.format(key))
    # Si c'est la touche ESC on sort du programme
    if (key == keyboard.Key.esc):
        #Stop.listener
        print("Sortie du programme")
        GPIO.cleanup()
        return False
 
# Le listener collecte les evenements et appelle les fonctions en callback
with keyboard.Listener(on_press = appui, on_release = relache) as listener:
    listener.join()

