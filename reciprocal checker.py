import random
from time import time
raw_input("Reciprocal Checker upto 3 decimal points!!!\nPress Enter to start...")
l = int(raw_input("Enter the lower range for practice : "))
u = int(raw_input("Enter the upper range for practice : "))
chance = 10
score = 0.0
while(chance>0):
	i = random.randint(l,u)
	start_time = time()
	ans = float(raw_input("\n\nReciprocal of "+str(i)+" = "))
	rec = round(1.0/i,3)
	if(ans == rec):
		end_time = time()
		print "\nRight!!"
		time_taken = int(end_time - start_time)
		if(time_taken<3):
						print("\nGood time response")
						score += 1
		if(time_taken>2 and time_taken<5):
						print("\nAverage time response")
						score += 0.7
		if(time_taken>4):
						print("\nBad time response")
						score += 0.5
	else:
		print "\nWrong!!\nRight Answer is "+str(rec)
	raw_input("\nPress enter to continue.....")
	chance -= 1
print "\n\nFinal Score = "+str(score)
