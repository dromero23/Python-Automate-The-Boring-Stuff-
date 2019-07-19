#!python3 
#pdfParanoiaReverse - goes through every pdf in a folder and decrypts the PDFs using a passowrd provided on the command line
import os,PyPDF2,sys,logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable(logging.CRITICAL)

def main():
	if len(sys.argv)<2 or not sys.argv[1].endswith('.pdf'):
		print('You didn\'t insert a pdfFile, usage: pdfPasswordBreaker.py [file.pdf]')
		sys.exit()
	textFile = open('dictionary.txt','r')
	passwords = [text.rstrip() for text in textFile]
	logging.debug(len(passwords))
	pdfFile = open(r'%s'%sys.argv[1],'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	if not pdfReader.isEncrypted:
		print('PDF does not have an encrypted password!')
		sys.exit()
	for password in passwords:
		logging.debug(str(password))
		if pdfReader.decrypt(str(password)):
			print('Password has been cracked! Password: %s'%str(password))
			sys.exit()
		elif pdfReader.decrypt(str(password).lower()):
			print('Password has been cracked! Password: %s'%str(password).lower())
			sys.exit()
	print('Unsuccesful password crack')
	
if __name__ == '__main__':
	main()