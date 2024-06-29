# DeezerAPI

A simple Python wrapper for the Deezer API, allowing easy access to a variety of Deezer's endpoints to fetch data about artists, albums, tracks, playlists, and more.

## Installation

To install the DeezerAPI module, simply use pip:

```bash
pip install deezer_api
```

## Usage

Below are examples of how to use the DeezerAPI module to access different types of data from Deezer.

### Importing and Initializing

```python
from deezer_api.deezer import DeezerAPI
```

### Initialize the API

```python
deezer = DeezerAPI()
```

### Search for an Artist
Search for an artist by name. For example, to search for "Eminem":

```python
results = deezer.search("eminem")
print(results)
```

### Get Album Information
Get information about a specific album by its ID. For example, to get the album with ID "302127":

```python
album_info = deezer.get_album("302127")
print(album_info)
```

### Get Editorial Information
Fetch the editorial information:

```python
editorial_info = deezer.get_editorial()
print(editorial_info)
```

### Get Chart Information
Fetch the chart information:

```python
chart_info = deezer.get_chart()
print(chart_info)
```

### Get Artist Information
Get information about a specific artist by their ID. For example, to get information about the artist with ID "27":

```python
artist_info = deezer.get_artist("27")
print(artist_info)
```

### Get Track Information
Get information about a specific track by its ID. For example, to get the track with ID "3135556":

```python
track_info = deezer.get_track("3135556")
print(track_info)
```










