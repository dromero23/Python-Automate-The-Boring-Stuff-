#!python3 
#renameDates.py - rename files with American style dates (MM-DD-YYYY) to European-style dates (DD-MM-YYYY)

import shutil, os,re

def main():
	# Create a regex that can identify the text pattern of Amerian-style dates
	datePattern = re.compile(r"""^(.*?)
	((0|1)?\d)-		# one or two digits for the month 
	((0|1|2|3)?\d)-	# one or two digits for the day 
	((19|20)\d\d)	#four digits for the year
	(.*?)$			#all text after the date
	""",re.VERBOSE)
	
	#TODO Call os.listdir() to find all the files in the working directory.
	for amerFilename in os.listdir('.'):
		mo = datePattern.search(amerFileName)
		#skip files without a date
		if mo == None: 
			continue 
		#Get the different parts of the filename
		beforePart = mo.group(1)
		monthPart = mo.group(2)
		dayPart = mo.group(4)
		yearPart = mo.group(6)
		afterPart = mo.group(8)
	#TODO Loop over each filename using the regex to check whether it has a date.
	
	#TODO If it has a date,rename the file with shutil.move()
	



if __name__ == '__main__':
	main()