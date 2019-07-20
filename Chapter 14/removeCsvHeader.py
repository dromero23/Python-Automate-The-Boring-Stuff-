#!python3 
#removeCsvHeader.py - removes the header from each CSV file and replaces with the current CSV file in the current working directory 
import os, logging, csv
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable(logging.CRITICAL)

def main():
#Find all the CSV files in the current working directory.
	for file in os.listdir('.'):
		if file.endswith('.csv'):
			logging.debug(file)
			#Read in the full contents of each file.
			cFile =open(file)
			cData = list(csv.reader(cFile))
			cFile.close()
			#Write out the contents, skipping the first line, to a new CSV file.
			print('Removing header from: ' +file)
			cFile = open(file,'w',newline='')
			outputWriter = csv.writer(cFile)
			for row in range(1,len(cData)):
				outputWriter.writerow(cData[row])
			cFile.close()

if __name__ == '__main__':
	main()