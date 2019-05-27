#!python3
#mp3DowntoMusic - moves all mp3 files from the download directory to the music directory 
import os,shutil

def main():
	for filename in os.listdir('C:\\Users\\Daniel\\Downloads'):
		if filename.endswith('.mp3'):
			print(filename + ' moving to C:\\Users\\Daniel\\Music' )
			shutil.move('C:\\Users\\Daniel\\Downloads\\' +filename, 'C:\\Users\\Daniel\\Music')



if __name__ == "__main__":
	main()