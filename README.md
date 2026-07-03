# exercice3-groupe3-jores


## 1- Gestion de bibliothèque en Python (CLI + POO)
Ce programme console a pour but de simuler une gestion des BIbliotheques classique

Il est strucure ainsi :
### book.py
Definition de la classe Livre (Book) de ses etats(attributs) et de ses actions (methodes)
### library.py
Definition de la classe library (Biblitontheque)

### main.py
Fichier principal a executer

## Comment lancer
utiliser la commande bash ou shell
```bash
    python main.py
```
si python n'est pas intalle l'installer


## 2 - Mini Application Meteo en HTML/CSS/JS fetch API
Cette application fonctionne comme suit il suffit d'entrer le nom d'une ville dans la zone de texte bpuis valider avec le bouton et soudain le nom de la ville s'affiche suivit des d'une icone qualificative de la meteo puis la temperature et enfin une mini description

### Description elle est strucree  comme suit:
### Le fichier index.html
Pour les blises et l'affichage du formulaire et des informatons meteorologiques
### Le fichier style.css
L'ajout de style pour une interface plus elegante
### Le fichier script.js
Pour la recuperation en API des informations meteorologique d'une ville donnee
## Comment lancer
Ouvrir le fichier `index.html` via le navigateur

# 3- Jeux de Quiz en HTML/CSS/JS
Ce projet vise a evaluer le niveau de culture de l'utilisateru via 10 quiz puis il calcule le score de cet utilisateur cet utilisateur a 4 propositions il en choisi une

## Structure

### index.html
Squelette du projet avec l'interface

### style.css
Fichier contenant le style pour la mise en page et la mise en forme du squette

## script.js
Le javascript contenant la logique de l'application tel que la definition des quizz l'utilisateur les evenements
## Comment lancer
Ouvrir le fichier index.html dans le navigateur
# 4- Csv analyzer en python via pandas
Ce projet vise a analyser (lire) un fichier csv et a effectuer des stats de base comme ventes total, et le produit le plus vendu

## Structure

### main.py
Fichier python contenant les fonctionnalitees de base

### sales.csv
Fichier contenant un exemple de csv pour une boutique avec les ventes par produit prix unitaire et quantite vendu

## Comment lancer
installer la librairie pandas 
```bash 
pip install pandas
```
puis executer la commande
```bash
    python main.py
```
# 5- Mini projet scraper python
Ce projet vise a extraire les informations json via une api publique dans une fichier python puis les ecrire dans un fichier json genere automatiquement. Et utiliser le fichier json avec la methode fetch via le javascript et afficher ses informations sous-forme de cartes dans le fichier html

## Structure
## scraper/main.py
Fichier principal python pour recuper les informations de l'API puis generer automatiquement le fichier `products.json`
### index.html
Squelette du projet avec l'interface

### style.css
Fichier contenant le style pour la mise en page et la mise en forme du squette

## script.js
Le javascript contenant la logique de l'application tel que la recuperation des informations du fichier json et leur affcihage sur le fichier html
## Comment lancer
Tout d'abord importer openfoodfacts pour ne pas avoir a ecrire l'url qui sera des lors obtenue automatiquement
Installer
```bash
pip install openfoodfacts
```
lancer et executer le fichier [main.py](mini-project/scraper/main.py)

puis ouvrir le fichier [index.html](mini-project/web/index.html) via le navigateur
