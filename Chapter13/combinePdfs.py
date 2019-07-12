#! python3
# combinePdfs.py - Combine all the PDFs in the current working directory into a single PDFs

import PyPDF2, os

def main():
	#Get all the PDF filenames.
	pdfFiles = []
	for filename in os.listdir('.'):
		if filename.endswith('.pdf'):
			pdfFiles.append(filename)
	pdfFiles.sort(key=str.lower)
	pdfWriter =PyPDF2.PdfFileWriter()

	#Loop through all the pdf files 
	for filename in pdfFiles:
		pdfFileObj = open(filename, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

		#Loop through all the pages (except the first) and add them 
		for pageNum in range(1, pdfReader.numPages):
			pdfWriter.addPage(pdfReader.getPage(pageNum))
	#Save the resulting PDF to a file.
	pdfOutputFile = open('allPdf.pdf','wb')
	pdfWriter.write(pdfOutputFile)
	pdfOutputFile.close()
	pdfFileObj.close()
if __name__ == '__main__':
	main()