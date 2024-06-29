# test.py

from deezer_api import DeezerAPI

deezer = DeezerAPI()

# Tester la recherche
result = deezer.search("eminem")
print("Search Results:", result)

# Tester la récupération d'un album
album = deezer.get_album("302127")
print("Album:", album)

# Tester la récupération des charts
charts = deezer.get_chart()
print("Charts:", charts)
