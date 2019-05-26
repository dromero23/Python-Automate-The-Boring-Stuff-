#!python3

#backupToZip.py - copies an entire folder and its contents into
#a ZIP file whose filename increments.

import zipfile, os,sys

def main():
	user_input = input('Enter the absolute folder path of your backup: ')
	backupToZip(r'%s'%(user_input))

def backupToZip(folder):
	#backup the the entire contents of "folder" into a ZIP file.
	python_dir = os.getcwd()
	os.chdir(folder)
	folder = os.path.split(os.getcwd())[1] # make sure folder the base name
	#Figure out the filename this colde should use based on 
	#what files already exist 
	number = 1
	while True: 
		zipFilename = os.path.basename(folder)+ '_'+str(number)+'.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1 
	# Create the ZIP file 
	print ('Creating %s...'%(zipFilename))
	backupZip = zipfile.ZipFile(zipFilename,'w')
	
	# Walk the entire folder tree and compress the files in each folder.
	for foldername,subfolders, filenames in os.walk('.'):
		if(foldername =='.'):
			continue
		print('Adding files in %s...'%(foldername))
		#add the current folder to the ZIP file.
		backupZip.write(foldername)
		#add all the files in this folder to the zip file.
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue #don't backup the backup ZIP files
			backupZip.write(os.path.join(foldername,filename))
	backupZip.close()
	os.chdir(python_dir) #change it back to the python directory 
	print('Done.')
	
if __name__ == '__main__':
	main()