# Spotify API

## Table des matières
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Compilation et lancement](#compilation-et-lancement)

## Introduction
Ce projet consiste à utiliser l'API Spotify afin de générer des playlists automatiquement.

Ce programme récupère l'entièreté des titres "likés" dans ma bibliothèque Spotify, les tri et les classe dans une playlist correspondant au mois auquel le titre a été liké.

Par exemple, la playlist créée appellée "Avril 2022" contiendra tous les titres que j'ai liké en avril 2022.

Ces playlists - du type "Mois Année" - sont ensuite ajoutées à mon compte Spotify.

## Technologies
Ce programme est 100% écrit en Python.
Il utilise la bibliothèque Python "Spotipy", elle-même conçue pour utiliser l'API Spotify.

## Compilation et lancement
Pour lancer le programme, il suffit d'exécuter "main.py".
Version utilisée pour tester le projet : Python 3.10.
