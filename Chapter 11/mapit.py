#!python 3
#mapit.py - Launches a map in the browser using an address from the 
#			command line or clipboard.

import webbrowser, sys, pyperclip 

def main():
	#Read the command line arguments from sys.argv.
	if len(sys.argv)>1:
		#get address from command line.
		address = ' '.join(sys.argv[1:])
		
	#: Read the clipboard contents.
	else: 
		address = pyperclip.paste()
	#Call the webbrowser.open() function to open the web browser.
	webbrowser.open('https://www.google.com/maps/place/' + address)



if __name__ == '__main__':
	main()
	
	
