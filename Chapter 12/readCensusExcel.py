#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for each county.

import openpyxl, pprint 

def main():
	print ('Opening workbook...')
	wb = openpyxl.load_workbook('censuespopdata.xlsx')
	sheet = wb['Popuplation by Census Tract']
	countyData = {}
	#TODO: Fill in countyData with each county's population and tracts.
	print('Reading rows...')
	for row in range(2,sheet.max_row+1):
		#Each row in the spreadsheet has data for one census tract.
		state  = sheet['B'+str(row)].value
		county = sheet['C'+str(row)].value
		pop    = sheet['D'+str(row)].value
		
		#TODO: Open a new text file and write the contents of countyData to it
if __name__ == '__main__':
	main()
