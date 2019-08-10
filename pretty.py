#! python3
# loading.py - Displays '.'
import time

#Get and print the mouse coordinates
def main():
	print('Press Ctrl-C to quit.')
	try: 
		print('Loading', end='')
		while True:
			for i in range(3):
				time.sleep(.5)
				print('.', end='',flush=True)
			time.sleep(.5)
			print ('\b'*3, end='', flush=True)
			print (' '*3, end='', flush=True)
			print ('\b'*3, end='', flush=True)
	except KeyboardInterrupt:
		print('\nDone.')
		
		
if __name__ =='__main__':
	main()