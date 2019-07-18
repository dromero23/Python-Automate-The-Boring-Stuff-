#!python3 
#pdfParanoia - goes through every pdf in a folder and encrypts the PDFs using a passowrd provided on the command line
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
				if pdfReader.isEncrypted:
					continue
				for pageNum in range(pdfReader.numPages):
					pdfWriter.addPage(pdfReader.getPage(pageNum))
				pdfWriter.encrypt(r'%s'%sys.argv[1] )
				fileN = filename.split('.')
				resultPDF = open(folderName+'\\'+fileN[0]+'_encrypted.pdf','wb')
				pdfWriter.write(resultPDF)
				resultPDF.close()
				pdfFile.close()
				
				#Read and decrypt the file before deleting the original
				pdfFile = open(folderName+'\\'+fileN[0]+'_encrypted.pdf','rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFile)
				#Delete the original(or display in the command line if you don't want to delete)
				if pdfReader.isEncrypted and pdfReader.decrypt(r'%s'%sys.argv[1]):
					#os.unlink(folderName+'\\'+filename)
					print('Deleting..' + filename +'from ' +folderName)
			

if __name__ == '__main__':
	main()