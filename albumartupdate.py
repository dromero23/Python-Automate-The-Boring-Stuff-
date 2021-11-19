import requests, json, sys, urllib
from PIL import Image

def main():
    specialChars = "\/:*?\"<>|"
    with open('mylist.txt') as f:
        albumidlist = f.readlines()
    for index, line in enumerate(albumidlist):
        albumid=line.replace("https://www.deezer.com/us/album/","")
        response = requests.get("https://api.deezer.com/album/"+albumid)
        albumdata = json.loads(response.text)
        albumcoverurl = albumdata['cover_xl']
        albumcoverurl = albumcoverurl.replace("1000x1000","1800x1800")
        jpgfilename = albumdata['title']
        for char in specialChars:
            jpgfilename = jpgfilename.replace(char,"")
        jpgfilename = jpgfilename+".jpg"
        urllib.request.urlretrieve(albumcoverurl,jpgfilename)
        #save album to embed properly to the flac/mp3 file
        im1 = Image.open(jpgfilename)
        im1 = im1.save(jpgfilename)
    
if __name__ == "__main__":
    main()