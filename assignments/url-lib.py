import urllib.request
import os

os.makedirs("downloads", exist_ok= True)

my_url = "https://gist.githubusercontent.com/Shoaib-Ashfaq/63305d9e33207ee1eb211ae69a828cc8/raw/7514bb7638f54ff71b094a6239672741d8b806da/family.csv"
urllib.request.urlretrieve(my_url, "downloads/family.csv")

print("Download Complete")
