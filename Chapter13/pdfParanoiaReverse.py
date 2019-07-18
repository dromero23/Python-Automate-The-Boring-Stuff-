#!python3 
#pdfParanoiaReverse - goes through every pdf in a folder and decrypts the PDFs using a passowrd provided on the command line
import os,PyPDF2, sys

def main():
	if len(sys.argv)<2:
		print('You didn\'t insert a password, usage: pdfParanoia.py [password]')
		sys.exit()
	pdfList =[]
	for folderName,subfolders, filenames in os.walk(r'C:\Users\dromero6\Documents\myPythonScripts\Chap_13'):
		for filename in filenames:
			if filename.endswith('.pdf'):
				pdfFile = open(folderName+'\\'+filename,'rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFile)
				pdfWriter = PyPDF2.PdfFileWriter()
				if not pdfReader.isEncrypted :
					continue
				if not pdfReader.decrypt(r'%s'%sys.argv[1]):
					print ('Unable to decrypt: ' + filename + ' from path: ' + folderName)
					continue
				for pageNum in range(pdfReader.numPages):
					pdfWriter.addPage(pdfReader.getPage(pageNum))
				fileN = filename.split('.')
				resultPDF = open(folderName+'\\'+fileN[0]+'_decrypted.pdf','wb')
				pdfWriter.write(resultPDF)
				resultPDF.close()
				pdfFile.close()
				

if __name__ == '__main__':
	main()