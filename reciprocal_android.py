import random
import sys
import time
import types
import sl4a
try:	
	import gdata.docs.service
except ImportError:
	gdata = None

droid = sl4a.Android()

def test_vibrate():
	result = droid.vibrate()
	return result.error is None


#
def test_alert_dialog(title, message):
	droid.dialogCreateAlert(title, message)
	droid.dialogSetPositiveButtonText('Continue')
	droid.dialogShow()
	response = droid.dialogGetResponse().result
	return response['which'] == 'positive'
#
def test_alert_dialog_with_buttons(title,message):
	droid.dialogCreateAlert(title, message)
	droid.dialogSetPositiveButtonText('Yes')
	droid.dialogSetNegativeButtonText('No')
	droid.dialogSetNeutralButtonText('Cancel')
	droid.dialogShow()
	response = droid.dialogGetResponse().result
	return response['which'] in ('positive', 'negative', 'neutral')


#
def test_alert_dialog_with_list():
	title = 'Alert'
	droid.dialogCreateAlert(title)
	droid.dialogSetItems(['foo', 'bar', 'baz'])
	droid.dialogShow()
	response = droid.dialogGetResponse().result
	return True

def test_make_toast(message):
	result = droid.makeToast(message)
	return result.error is None
sys.stdout.flush()

test_alert_dialog("Reciprocal Checker upto 3 decimal points!!!")
sys.stdout.flush()
l = int(droid.dialogGetInput('lower range').result)
sys.stdout.flush()
u = int(droid.dialogGetInput('upper range').result)
chance = 10
score = 0.0
while(chance>0):
	i = random.randint(l,u)
	start_time = time()
	sys.stdout.flush()
	ans = 1
	rec = round(1.0/i,3)
	if(ans == rec):
		end_time = time()
		#print "\nRight!!"
		time_taken = int(end_time - start_time)
		sys.stdout.flush()
		if(time_taken<3):
			test_make_toast("Good time response")
			score += 1
		if(time_taken>2 and time_taken<5):
			test_make_toast("Average time response")
			score += 0.7
		if(time_taken>4):
			test_make_toast("Bad time response")
			score += 0.5
	else:
		#print "\nWrong!!\nRight Answer is "+str(rec)
	#raw_input("\nPress enter to continue.....")
	chance -= 1

#print "\n\nFinal Score = "+str(score)
