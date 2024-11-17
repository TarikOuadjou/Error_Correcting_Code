# Code Cyclique - Correcteur d'Erreur

## Description du projet

Ce projet met en œuvre un **code correcteur d'erreurs** basé sur des **codes cycliques**. Ces codes sont couramment utilisés pour détecter et corriger les erreurs pouvant survenir lors de la transmission de données. Le code utilise un polynôme générateur \( g(x) \) pour encoder les données et applique un algorithme de décodage pour tenter de restaurer les données originales, même en présence d'erreurs.  

Deux approches sont proposées :
- Une représentation des polynômes via des listes.
- Une représentation des polynômes via des entiers, utilisant leur codage binaire.

## Objectifs

- **Encodage d'images** : Ajouter une protection contre les erreurs en encodant chaque pixel de l'image avec un code cyclique.
- **Simulation d'erreurs** : Introduire des erreurs aléatoires sur l'image encodée pour simuler des erreurs de transmission.
- **Décodage et correction** : Utiliser un algorithme correcteur pour récupérer l'image d'origine, corrigée autant que possible.

## Fonctionnalités principales

- **Encodage** : Chaque pixel de l'image est transformé en un code protégé par un polynôme générateur.
- **Ajout d'erreurs** : Des altérations sont appliquées de manière aléatoire aux pixels encodés pour reproduire des erreurs de transmission.
- **Décodage** : L'algorithme correcteur tente de détecter et de corriger ces erreurs pour retrouver les valeurs d'origine.

## Prérequis

Avant d'exécuter ce projet, assurez-vous d'avoir les bibliothèques suivantes installées :  

- `Pillow (PIL)` : Pour le traitement des images.  
- `random` : Pour simuler des erreurs aléatoires.  
- `os` : Pour la gestion des fichiers.  

Installez Pillow avec la commande suivante :  

```bash
pip install pillow
