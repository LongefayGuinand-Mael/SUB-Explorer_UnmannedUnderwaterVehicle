<br>
	<p align="center">
		<h1 align="center"> :warning:   WARNING   :warning: </h1>
	</p>
	<p align="center">
		This project was made in French only for an Academic Work. So please consider that whole project files names, reports and other are only in French.
		This project was made during our last year in the ESME Sudria Engineering School between October 2022 and March 2023.
	</p>
<br>





------------------------------------------------------

<br>
	<p align="center">
	    <h1 align="center">Unmanned Underwater Vehicle - Sub-Explorer</h1>
	</p>
</br>
Dans le cadre de notre dernière année academic d'ingénierie à l'ESME Sudria (Master 2), mon groupe et moi-même avons travaillé pendant une durée de 6 mois sur un drone sous-marin ayant pour objectif principal la recherche scientifique. Dans le cadre de notre projet, nous avons mis en place diverses choses afin de mener à bien cet objectif et nous sommes arrivé à un résultat très concluant.   

Ce projet c'est principalement articulé avec les parties suivantes :
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

<br>
	<p align="center">
	    <h2 align="center">Définition du Cahier des Charges</h2>
	</p>
</br>

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

<br>
	<p align="center">
	    <h2 align="center">Choix des Composants</h2>
	</p>
</br>

*Toutes les datasheets des composants utilisés sont regroupées dans les fichiers du projet dans le dossier `/DatasheetsComposents`.*

### Intelligences Numériques :
Nous utilisons dans ce projet 2 Raspberry Pi.   
- La première est une **Rasberry Pi 4B (de 4 à 8 Go RAM)**. Cette Raspberry Pi nous permet la réception des données envoyées par la télécommande et donc par l'utilisateur afin de contrôler les moteurs et l'allumage ou non des LED qu'il embarque.   
- La seconde est une **Raspberry Pi 3B+**. Cette Raspberry Pi, quant-à elle, nous permet d'éberger un WebServeur local afin d'avoir un retour caméra et capteurs (afin de connaître, même si nous ne voyons plus le drone depuis la surface, de connaître l'environnement dans lequel il est).

### Caméra Embarquée :
Comme dit plus haut, nous avons besoin de savoir consatemment l'environnement du drone même lorsque celui-ci n'est pas visible depuis la surface. Ainsi, nous utilisons une caméra embarquée dans le drone. Par soucis de simplicité et surtout de qualité, nous avons choisi de prendre la **Camera Module V2 Raspberry** (existe maintenant également avec un autofocus). Cette caméra embarqué nous permet d'avoir une excélente qualité (1280x720 pixel) avec un haut débit (jusqu'à 24 fps) et puis elle est nativement supportée par la Rasberry Pi 3B+ qui va l'utiliser et envoyer son stream vidéo sur le WebServeur qu'elle host.

### Récepteur Radio + Télécommande :
Dans notre projet, nous avons eu la volonté de contrôler notre drone à distance en imaginant un moyen d'éviter d'avoir un drone qui embarque un enrouleur de câble pour pouvoir communiquer avec l'utilisateur via ce qui s'apparente à un câble d'Arianne. Ainsi, nous avons choisi de mettre en place ce câble d'Arianne entre notre sous-marin et un flotteur. Ce flotteur pourra ainsi embarquer 2 antennes. L'une étant l'antenne radio (2.4GHz) et l'autre une antenne WiFi (dont nous reparlerons plus tard).

Nous avons donc prit un récepteur radio **FS-IA6B**. Ce récepteur 2.4GHz (fréquence laissée libre pour la science et d'autres recherche) va nous servirà communiquer avec notre sous-marin. En plus de ce récepteur, nous avons une télécommande FlySky (utilisée dans le modélisme et qui convient très bien à notre projet pour le moment). 

### Composants ayant un lien avec le déplacement du drone :
La phase la plus technique dans ce projet est le déplacement du sous-marin car en plus de la réception des données de la télécommande redio, il faut adapter les données récupérées en données fiables pour contrôler convenablement nos moteurs. 

Nous avons 2 types de moteurs : 
- 4 moteurs pas-à-pas **17HS08-1004S** commandé à l'aide d'un driver moteur **A4988-1182** par la Raspberry Pi 4B.
- 1 moteur à courant continu de la marque **lichifit** (utilisé dans le modélisme naval) commandé à l'aide d'un driver moteur **DRV8838** également par la Raspberry Pi 4B.

Les moteurs pas-à-pas seront utilisés pour des mouvements plus précis tels que les mouvements translatifs lattéraux et de profondeur et pour les mouvement rotatifs (lacet et tangage).    
Le moteur à courant continu sera quant-à lui utilisé uniquement pour la translation avant-arrière et sera notre propulseur principal.

### Composants ayant un lien avec la récupération de données (capteurs) :
Dans notre sous-marin, nous souhaiton à minima pouvoir récupérer deux données, la température et la pression. 

Pour le capteur de température, nous avons choisi le capteur **DS18B20**. Le choix de ce composant à été assez intuitif puisque celui-ci ressemble à une sonde, il est étanche et à une plage d'utilisation large avec une précision de 0.0625°C.

Pour le capteur de pression, nous avons choisi le capteur **MS5837-30BA**. Ce capteur fonctionne en I²C, il est étanche et a une plage de fonctionnement allant jusqu'à 30 bar (jusqu'à 290m de profondeur dans l'eau) avec une précision de 0.2mBar (soit ±2mm).

À l'avenir, nous imaginons pouvoir rajouter des capteurs tels que celui de salénité de l'eau et de pollution maritime ou encore un capteur de tangage pour la stabilisation du drone.

### Composants autres :
Les autres composants sont divers. 

Nous avons ici un convertisseur Buck-Boost **DFR0753** afin de pouvoir allimenter d'une tension de 5V les 2 Raspberry Pi mais d'une tension de 9V les différents moteurs et le bandeau LED.

En parlant du **bandeau LED**, nous avons imaginé embarquer des LED dans le sous-marin afin de permettre de les activer ou non pour pouvoir, en toutes circonstances et sur demande de l'utilisateur, de voir l'environnement de travail du drone sous-marin qu'il soit visible depuis la surface ou pas. Le bandeau LED est unicolore blanc, certifié IP67 (étanche poussière et eau), et peut être allimenté jusqu'à 12V. Nous l'utilisons avec une tension d'allimentation de 9V largement suffisante pour nous.





<a name="schémas-électroniques"></a>
------------------------------------------------------

<br>
	<p align="center">
	    <h2 align="center">Schémas Électroniques</h2>
	</p>
</br>

*Pour une meilleure qualité, les images des schémas électroniques sont trouvables dans les fichiers du projet dans le dossier `/SchémasÉlectroniques+PCB`) Leurs noms étants : `Schéma Électronique - Raspberry Pi 3B+.png` et `Schéma Électronique - Raspberry Pi 4B.png`.*

Après l'analyse de tous les composants, nous avons mis en place 2 schémas électroniques. L'un concerne la Raspberry Pi 3B+ et l'autre la Raspberry Pi 4B.

### Partie Raspberry Pi 3B+ :

Pour cette partie, nous retrouvons dans le schéma électronique les capteurs de température et de pression. Il est à noté également que nous avons de géré par cette Raspberry Pi la caméra embarquée.

<img width="789" alt="Schéma Électronique - Raspberry Pi 3B+" src="https://user-images.githubusercontent.com/80823327/229891498-533df845-b693-444f-bc66-fd88b1f937c3.png">

### Partie Raspberry Pi 4B :

Pour cette partie, nous retrouvons dans le schéma électronique les 4 moteurs pas-à-pas ainsi que leurs drivers respectifs, le moteur à courant continu et son driver, le bandeau LED, le récepteur 2.4GHz et des pins de branchement pour le convertisseur Buck-Boost (9V à 5V). 

<img width="869" alt="Schéma Électronique - Raspberry Pi 4B" src="https://user-images.githubusercontent.com/80823327/229891526-37f326ff-b1fe-45c6-b2dd-10d3bc880dd1.png">

***À Noter :*** *Les fichiers Fusion360 ayants permis de faire les schémas électroniques ainsi que les PCB sont trouvables dans les fichiers du projet dans le dossier `/SchémasÉlectroniques+PCB/FichiersFusion`.*





<a name="pcb"></a>
------------------------------------------------------

<br>
	<p align="center">
	    <h2 align="center">Réalisation des Printed Circuit Board (PCB)</h2>
	</p>
</br>

*Fichiers de conception des PCB sont trouvables dans les fichiers du projet dans le dossier `/SchémasÉlectroniques+PCB/FichiersConceptionPCB`. Un dossier regroupe les fichiers utiles par un fabriquant de PCB pour faire celui de la Raspberry Pi 3B+ et un autre dossier est pour celui de la Raspberry Pi 4B.*

Cette partie ne pourra pas être beaucoup développée à l'écrit. Pour faire au plus simple, suite à la mise en place de nos 2 schémas électroniques, nous avons pu mettre en place 2 PCB qui seront utilisés pour notre projet (un pour chacune des intelligences électroniques). Sur le PCB de la Raspberry Pi 3B+ on peut y retrouver les branchements des différents capteurs tandis que sur le PCB de la Raspberry Pi 4B on y retrouve tous les composants utiles pour la réceptions des commandes de l'utilisateurs et les différents systèmes et branchements pour les moteurs et bandeau LED (en outre, tout ce qui est contrôllable par l'utilisateur à distance). 

La seconde chose importante mise en place est la définition de contraintes de dimentionnement afin de permettre aux 2 PCB de se brancher directement sur les Raspberry Pi. Ces contraintes sont principalement liée aux composants internes des Raspberry Pi et leurs hauteurs qui peuvent être génantes (dans les grandes lignes, ça regroupe les composants tels que celle du port éthernet, des ports USB, port de branchement caméra, port Jack et HDMI).

***Rappel :*** *Les fichiers Fusion360 ayants permis de faire les schémas électroniques ainsi que les PCB sont trouvables dans les fichiers du projet dans le dossier `/SchémasÉlectroniques+PCB/FichiersFusion`.*





<a name="programmation"></a>
------------------------------------------------------

<br>
	<p align="center">
	    <h2 align="center">Programmation (Python)</h2>
	</p>
</br>

*Tous les fichiers de programmation sont regroupées dans les fichiers du projet dans le dossier `/Programmation/Code`. Dans ce dossier on peut y retrouver les codes en Python (`.py`) ainsi que des logigrammes des programmes (au format `.png`).* 

Pour commencer, nous avons 2 intelligences numériques (1 Raspberry Pi 3B+ & 1 Raspberry Pi 4B) qui vont fonctionner simultannément mais de manière totalement distincte l'une de l'autre. Ainsi, nous exposons ci-dessous les logigrammes des programmes des 2 intelligences numériques : 

### Partie Raspberry Pi 3B+ :

<img width="936" alt="Logigramme Raspberry Pi 3B+ - SUB-Explorer" src="https://user-images.githubusercontent.com/80823327/229874723-092826c4-6eda-41ee-9172-262b14647ec6.png">

Nous pouvons retrouver 2 étapes, l'initialisation et le fonctionnement. L'initialisation nous permet d'instancier les divers pins de la Raspberry que nous utilisons par la suite dans notre code ainsi que les multiples librairies utilisées. La phase de fonctionnement permet l'hébergement et l'envoie du stream de la caméra embarquée sur le WebServeur local de la Raspberry Pi 3B+. Il sera possible par la suite de créer un multi-thread afin de pouvoir récupérer en parallèle du WebServeur des données de capteurs pour les ajouter au retour caméra sur la page Web hébergée (*un début de code dans ce sens est retrouvable sous le nom `TempPrint_CameraWebLocal.py`*).

### Partie Raspberry Pi 4B :

![Logigramme Pi4B (1) - SUB-Explorer](https://user-images.githubusercontent.com/80823327/229874655-cd82081b-62a3-4f2f-bb31-14f6707dc589.png)

Tout comme pour la Raspberry Pi 3B+, nous pouvons y voir qu'il y a 2 étapes dans ce logigramme, l'initialisation et le fonctionnement en temps-réel avec la mise en place d'un multi-thread ce qui équivaut à l'utilisation de plusieurs coeurs du processeur de la Raspberry Pi 4B qui se charge de ce code. *On peut également retrouver le programme de récupération des données réceptionnées depuis la télécommande radio sur le logigramme `Logigramme Pi4B (2) - SUB-Explorer.png` mit dans le fichier `/Programmation/LogigrammesExplicatifs/`.*





<a name="modélisation-3d"></a>
------------------------------------------------------

<br>
	<p align="center">
	    <h2 align="center">Modélisation Structurelle du Drone</h2>
	</p>
</br>

Voici une image de l'assemblage total des pièces imprimées en 3D de notre drone : 

![UUV](https://user-images.githubusercontent.com/80823327/229297162-fc86d0dc-1c18-4dbe-95bb-5cfa39f9e808.png)

*Pour une meilleure qualité, l’image de l'assemblage de la modélisation structurelle du drone sont trouvables dans les fichiers du projet (au niveau de la racine). Son nom étant : `Assemblage3D.png`.*   


Voici également une vidéo montrant l'**ordre assemblage des quelques 28 pièces (_vis non-incluses_)** composants notre sous-marin : 

https://user-images.githubusercontent.com/80823327/229296633-9bad1075-d35f-4a4c-87c2-66e0a59497dc.mp4
   
**Concernant les fichiers 3D de chacune des pièces ainsi que de l'assemblage, ces fichiers sont trouvables dans les fichiers du projet dans le dossier `/Modélisation3D`.**





<a name="contacts"></a>
------------------------------------------------------

<br>
	<p align="center">
	    <h2 align="center">Noms et Contacts</h2>
	</p>
</br>

[![Linkedin Badge](https://img.shields.io/badge/M._LONGEFAY_Mael-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mael-longefay-guinand/)
[![Linkedin Badge](https://img.shields.io/badge/M._PIOT_Fabien-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fabien-piot/) 
[![Linkedin Badge](https://img.shields.io/badge/M._POPESCO_Jules-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jules-popesco/) 




-------------------------------------
-------------------------------------
## License
***© COPYRIGHT - All Rights Reserved - Zapata Industry (LONGEFAY-PIOT-POPESCO)***  
***Important :*** *Afin de poursuivre le projet, merci de nous contacter sur LinkedIn pour avoir notre approbation.*
