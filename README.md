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
deezer = DeezerAPI()


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
