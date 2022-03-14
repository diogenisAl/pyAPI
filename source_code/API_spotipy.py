import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
                             client_id='INSERT PUBLIC TOKEN HERE',
                             client_secret='INSERT SECRET TOKEN HERE')
                         )
name = input("Select an artist you like: ")

# Get artist json using the search function.
# It returns a dict containing all the artists tha fit the search
artist_res = spotify.search(q='artist:' + name, type='artist')
# print(json.dumps(artist_res, indent=4))

#  Get a dict of the items in the artist json.
# 'artists' is the key that holds all data in the json and
# 'items' holds the individual records of the artists
items = artist_res['artists']['items']
# print(json.dumps(items, indent=4))

# Check if the search found an artist with that name
while len(items) == 0:
    print("No artist", name, "found")
    name = input("Try again: ")
artist_uri = items[0]['uri']
# print(artist_uri)

print("If you like", name, "you should give a listen to:")

# Get related artists from the API using the preffered artist's uri
related_artists = spotify.artist_related_artists(artist_uri)
# print(type(related_artists))
# print(related_artists.keys())

# Get the artists' dictionaries from the response dict
related_artists = related_artists['artists']
# print(type(related_artists))
# print(related_artists.keys())

# Gather all related artists' ids
related_artists_ids = []
for artist in related_artists:
#     print(artist['name'])
    related_artists_ids.append(artist['id'])

related_albums = []

# For each artist get their most popular album
for i in range(10):
    artist_id = related_artists_ids[i]
    results = spotify.artist_albums(artist_id, limit=1)
    album = results['items'][0]['name']
    related_albums.append(album)
    print(album, "by", spotify.artist(artist_id)['name'])

# TODO print the artist's top songs in Greece, Italy, Spain and Canada
