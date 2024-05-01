# Spotify Monthly Playlist Generator

## Table of Contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Installation and Usage](#installation-and-usage)

## Introduction
The Spotify Monthly Playlist Generator is a Python application designed to automate the creation of playlists based on liked tracks in a user's Spotify library. It categorizes tracks by the month they were liked and generates playlists accordingly.

## Technologies
The application is written in Python and utilizes the Spotipy library to interact with the Spotify API. Tested on Python@3.12.0 with librairies listed in `requirements.txt`.

## Installation and Usage
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Ensure you have a Spotify developer account and obtain the necessary API credentials.
4. Add a JSON file as `./keys/api_keys.json`: `{"CLIENT_ID": "your_spotify_client_id", "CLIENT_SECRET": "your_spotify_client_secret"}`
5. Run the program by executing `python main.py "your_spotify_username"`.
6. Follow the prompts to authorize the application to access your Spotify account and generate playlists.
7. Playlists with the format "Month Year" will be created and added to your Spotify account automatically.
