#! python3 
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square & adds catlogo.png to the lower-right corner.
import os 
from PIL import Image 

SQUARE_FIT_SIZE = 300
RESIZE = 13 #for the catlogo.png, note: image is larger than 300 pixels
LOGO_FILENAME = 'catlogo.png'

def main():
	logoIm = Image.open(LOGO_FILENAME)
	logoWidth, logoHeight = logoIm.size
	logoWidth = int(logoWidth/RESIZE)
	logoHeight = int(logoHeight/RESIZE)
	resizeLogo = logoIm.resize((logoWidth, logoHeight))
	resizeLogo.save (os.path.join('withLogo', LOGO_FILENAME))
	os.makedirs('withLogo', exist_ok=True)
	#Loop over all files in the working directory.
	for filename in os.listdir('.//watermark'):
		if not (filename.endswith('.png') or filename.endswith('.jpg'))  or filename == LOGO_FILENAME:
			continue #skip non-image files and the logo itself
		im = Image.open(os.path.join('watermark', filename))
		width, height = im.size 
		#Check if image needs to be resized
		if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
			#Calculate the new width and height to resize to.
			if width> height:
				height = int( ( height/width) *SQUARE_FIT_SIZE)
				width = SQUARE_FIT_SIZE
			else: 
				width = int( (width/height) * SQUARE_FIT_SIZE ) 
				height = SQUARE_FIT_SIZE
		#Resize the image. 
		print( ' Resizing %s ...' %(filename))
		print('Size... width: %s height: %s' %(width-logoWidth,height-logoHeight))
		im = im.resize ( (width,height))
		#Add the logo
		print( ' Adding logo to %s' %(filename) )
		pastew = width - logoWidth
		pasteh = height - logoHeight
		im.paste(resizeLogo, (pastew, pasteh),resizeLogo)
		#Save the changes
		im.save (os.path.join('withLogo', filename))

if __name__ == '__main__':
	main()
