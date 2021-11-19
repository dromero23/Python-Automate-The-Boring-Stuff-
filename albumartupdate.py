import requests, json, sys, urllib
from PIL import Image

def main():
    with open('mylist.txt') as f:
        albumidlist = f.readlines()
    for index, line in enumerate(albumidlist):
        albumid=line.replace("https://www.deezer.com/us/album/","")
        response = requests.get("https://api.deezer.com/album/"+albumid)
        albumdata = json.loads(response.text)
        albumcoverurl = albumdata['cover_xl']
        albumcoverurl = albumcoverurl.replace("1000x1000","1800x1800")
        urllib.request.urlretrieve(albumcoverurl,albumdata['title']+ ".jpg")
    
if __name__ == "__main__":
    main()