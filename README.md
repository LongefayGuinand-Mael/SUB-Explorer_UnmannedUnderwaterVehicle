:warning: `  WARNING  ` :warning:   
This project was made in French only for an Academic Work. So please consider that whole project files names, reports and other are only in French.
This project was made during my last year in the ESME Sudria Engineering School between October 2022 and March 2023.

------------------------------------------------------
# Unmanned Underwater Vehicle - Sub-Explorer
Dans le cadre de notre dernière année academic d'ingénierie à l'ESME Sudria (Master 2), mon groupe et moi-même avons travaillé pendant une durée de 6 mois sur un drone sous-marin ayant pour objectif principal la recherche scientifique. Dans le cadre de notre projet, nous avons mis en place diverses choses afin de mener à bien cet objectif et nous sommes arrivé à un résultat très concluant.

_Ce projet c'est principalement articulé avec les parties suivantes :_
	- Définition du Cahier des charges 
	- Veille technologique :
		- Recherche des Composants
		- Mise en place d'un schéma électrique
		- Réalisation des Printed Circuit Board
	- Programmation (Python)
	- Modélisation structurelle 3D du drone
*Les autres parties (moins techniques) sont trouvables dans le rapport complet de notre projet de fin d'études.*

------------------------------------------------------

### Sommaire :
1. [Définition du Cahier des Charges](#cahier-des-charges)
2. [Choix des Composants](#choix-composants)
3. [Schémas Électroniques](#schémas-électroniques)
4. [Réalisation des Printed Circuit Board (PCB)](#pcb)
5. [Programmation](#programmation)
6. [Modélisation structurelle du drone](#modélisation-3d)
7. [Noms et Contacts des étudiants ayant travaillé sur le projet](#contacts)

<a name="cahier-des-charges"></a>
------------------------------------------------------



## Définition du Cahier des Charges :
### Introduction :
Notre objectif principal est de mettre au point un système de pilotage efficace pour notre drone sous-marin, en veillant à sa motorisation directionnelle et à sa radiocommunication. Nous prévoyons également d'intégrer des outils scientifiques à notre plateforme, ainsi que de travailler sur l'optimisation de son design. En somme, ce projet est l'opportunité pour nous de mettre en pratique nos connaissances en matière de systèmes embarqués, tout en nous confrontant à des défis technologiques passionnants.
Dans le cadre de ce projet, nous mettons d’abord la priorité sur le pilotage de la plateforme (motorisation directionnelle, radiocommunication). Les outils scientifiques et l’optimisation du design seront vus dans un second temps.

### Fonctionnalités :
1. _Les fonctionnalités primaires :_
	- UUV manœuvrable sur 3 dimensions. → Motorisation directionnelle (lacet, tangage, profondeur, direction).
	- L’UUV est radiocommandé. → Conception d’un flotteur permettant de maintenir l’antenne (récepteur 2.4GHz) hors de l’eau afin de simplifier la communication entre le système de pilotage et la machine.
→ Utilisation d’une télécommande et d’un récepteur 2.4GHz.
	- Le drone doit être étanche afin de protéger le système de l’eau.
	- Le drone doit également répondre à une limite de taille afin qu'il puisse se déplacer dans des espaces restreints. Nous avons donc pour objectif de taille que le drone fasse maximum 600 mm de longueur et 300 mm de diamètre.
	- La flottaison de l’UUV doit être neutre : nous devons faire en sorte d’obtenir un équilibre entre le poids et la poussée d’Archimède du drone.
	- Nous voulons que le drone puisse effectuer des missions scientifiques d’une durée minimum de 30 minutes - 1 heure. Cela nous défini une contrainte d'autonomie.
2. _Les fonctionnalités secondaires :_
	- Retour vidéo (mise en place d’une caméra embarquée pour pouvoir voir ce qui se trouve dans l’environnement du drone même lorsque celui-ci n'est pas visible depuis la surface).
	- Système d’éclairage LED afin de pouvoir voir convenablement l’environnement où se trouve le drone via le retour caméra.
	- Capteurs de température et de pression (utile pour de la recherche et pour assurer le maintien structurel du drône en fonction de la pression exercée sur lui de part la pression de l’eau - liée à la profondeur à laquelle il se trouve).
	- Structure résistante aux chocs et protégeant les composants fragiles pouvant être exposés à l’extérieur du drone (par exemple les capteurs ou encore les hélices des moteurs).
3. _Les fonctionnalités intéressantes supplémentaires :_
	- Ajout de systèmes pour la collecte de données scientifiques : échantillonneur, sondeur, GPS, divers nouveau capteur, etc.
	- Intégrer une capacité de stockage et de récupération rapide des données.
	- Développement d’une application mobile pour le pilotage de tout le drone (contrôle de
son déplacement dans l’espace et des éléments scientifiques qu’il embarque et permettant l’affichage du flux vidéo en temps réel).

### Schéma Bloc Fonctionnel du Projet :

<img width="949" alt="SchémaBlocFonctionel" src="https://user-images.githubusercontent.com/80823327/229297224-abcfcb5b-b0a2-4196-a7e3-12d45499c083.png">


<a name="choix-composants"></a>
------------------------------------------------------

## Choix des Composants :
*Toutes les datasheets des composants utilisés sont regroupées dans les fichiers du projet dans le dossier `/DatasheetsComposents`. Leurs noms étants : `SchémaÉlectroniqueRaspPi4B.png` et  `SchémaÉlectroniqueRaspPi3B+.png`.*
### Intelligences Numériques :
### Caméra Embarquée :
### Récepteur Radio + Télécommande :
### Composants ayant un lien avec le déplacement du drone :
### Composants ayant un lien avec la récupération de données (capteurs) :
### Composants autres :


<a name="schémas-électroniques"></a>
------------------------------------------------------

## Schémas Électroniques :
*Pour une meilleure qualité, les images des schémas électroniques sont trouvables dans les fichiers du projet dans le dossier `/SchémasÉlectroniques+PCB`) Leurs noms étants : `SchémaÉlectroniqueRaspPi4B.png` et  `SchémaÉlectroniqueRaspPi3B+.png`.*

//////// BLABLA + IMAGES ////////

***À Noter :*** *Les fichiers Fusion360 ayants permis de faire les schémas électroniques ainsi que les PCB sont trouvables dans les fichiers du projet dans le dossier `/SchémasÉlectroniques+PCB/FichiersFusion`.*


<a name="pcb"></a>
------------------------------------------------------

## Réalisation des Printed Circuit Board (PCB) :
*Fichiers de conception des PCB sont trouvables dans les fichiers du projet dans le dossier `/SchémasÉlectroniques+PCB/FichiersConceptionPCB`. Un dossier regroupe les fichiers utiles par un fabriquant de PCB pour faire celui de la Raspberry Pi 3B+ et un autre dossier est pour celui de la Raspberry Pi 4B.*

//////// BLABLA ////////

***Rappel :*** *Les fichiers Fusion360 ayants permis de faire les schémas électroniques ainsi que les PCB sont trouvables dans les fichiers du projet dans le dossier `/SchémasÉlectroniques+PCB/FichiersFusion`.*


<a name="programmation"></a>
------------------------------------------------------

## Programmation (Python) :
*Tous les fichiers de programmation sont regroupées dans les fichiers du projet dans le dossier `/Programmation/Code`.*

//////// BLABLA + IMAGE LOGIGRAMMES + BLABLA ////////

<a name="modélisation-3d"></a>
------------------------------------------------------

## Modélisation Structurelle du Drone :
Voici une image de l'assemblage total des pièces imprimées en 3D de notre drone : 

![UUV](https://user-images.githubusercontent.com/80823327/229297162-fc86d0dc-1c18-4dbe-95bb-5cfa39f9e808.png)

*Pour une meilleure qualité, l’image de l'assemblage de la modélisation structurelle du drone sont trouvables dans les fichiers du projet (au niveau de la racine). Son nom étant : `Assemblage3D.png`.*   


Voici également une vidéo montrant l'**ordre assemblage des quelques 28 pièces (_vis non-incluses_)** composants notre sous-marin : 

https://user-images.githubusercontent.com/80823327/229296633-9bad1075-d35f-4a4c-87c2-66e0a59497dc.mp4
   
**Concernant les fichiers 3D de chacune des pièces ainsi que de l'assemblage, ces fichiers sont trouvables dans les fichiers du projet dans le dossier `/Modélisation3D`.**


<a name="contacts"></a>
------------------------------------------------------

## Noms et Contacts :
[![Linkedin Badge](https://img.shields.io/badge/M._LONGEFAY_Mael-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mael-longefay-guinand/)
[![Linkedin Badge](https://img.shields.io/badge/M._PIOT_Fabien-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fabien-piot/) 
[![Linkedin Badge](https://img.shields.io/badge/M._POPESCO_Jules-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jules-popesco/) 

-------------------------------------
-------------------------------------
## License
***© COPYRIGHT - All Rights Reserved - LONGEFAY-PIOT-POPESCO***  
*_Important :_ Afin de poursuivre le projet, merci de nous contacter sur LinkedIn pour avoir notre approbation.*
