from selenium import webdriver
import pyautogui
import time
import win32clipboard
#phantomjs_path = "phantomjs.exe"
chrome_path = "chromedriver.exe"
#browser = webdriver.PhantomJS(phantomjs_path)
browser=webdriver.Chrome(chrome_path)
browser.implicitly_wait(10)

def enterUserID(ticket,idt,firstTime):
	time.sleep(5)
	if(firstTime == 1):
		browser.find_element_by_xpath("/html/body/div/header/div[1]/div/div[2]/div/div[4]/form/div/label/span").click()
	browser.switch_to_default_content()
	searchBox = browser.find_element_by_xpath("//*[@id=\"sysparm_search\"]")
	searchBox.click()
	pyautogui.hotkey('ctrl','a')
	time.sleep(0.25)
	searchBox.send_keys(ticket)
	time.sleep(1)
	pyautogui.press('\n')
	browser.switch_to.frame("gsft_main");	
	state = browser.find_element_by_xpath("//*[@id=\"incident.state\"]")
	state.click()
	pyautogui.press('W')
	pyautogui.press('\t')
	browser.find_element_by_xpath("//*[@id=\"sys_display.incident.assigned_to\"]").click()
	browser.find_element_by_xpath("//*[@id=\"sys_display.incident.assigned_to\"]").send_keys(idt)
	time.sleep(3)
	pyautogui.press('\t')
	browser.find_element_by_xpath("//*[@id=\"sysverb_update\"]").click()

def userLogin():
	browser.get('link')
	user=browser.find_element_by_css_selector("#username")
	user.send_keys('username')
	password=browser.find_element_by_css_selector("#password")
	password.send_keys('password')
	domain=browser.find_element_by_css_selector("#domain")
	pyautogui.press('\t')
	pyautogui.press('A')
	time.sleep(1)
	login2=browser.find_element_by_xpath("//*[@id=\"buttonHolder\"]/input[7]")
	login2.click()

if __name__ == "__main__":
		userLogin()
		win32clipboard.OpenClipboard()
		data = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		allId = data.splitlines()
		ad = 'Amit Dey'
		vm = 'Vivek Mohanty'
		rn = 'Rohan Nair'
		i=1
		firstTime = 1
		for ticket in allId:
			idt = ad
			enterUserID(ticket,idt,firstTime)
			firstTime = 0
		browser.close()
