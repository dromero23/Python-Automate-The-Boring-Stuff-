#!python3 
# stopwatch.py - A simple stopwatch program 
import time 
#Display the program's instructions. 

def main():
	print('Press ENTER to begin. Aftewards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
	input()
	print('Started.')
	startTime = time.time() #get the first lap's start time 
	lastTime = startTime
	lapNum = 1 
	print('Lap Number:   Total time 	(LapTime)')
	try: 
		while True: 
			input()
			lapTime = round(time.time()- lastTime, 2)
			totalTime = round(time.time() - startTime, 2)
			print('Lap #%s: 	%s 		(%s) ' %(lapNum, totalTime, lapTime), end ='')
			lapNum += 1
			lastTime = time.time() #reset last lap time
	except KeyboardInterrupt: 
		#Handle the Ctrl-x exception to keep its error message from displaying 
		print('\nDone.')

if __name__ =='__main__':
	main()
