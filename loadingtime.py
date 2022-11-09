from urllib.request import urlopen
from time import time

#obtaining the url of website
website = urlopen('https://www.instagram.com/')

#return the number of seconds passed since epoch
open_time =time()

#read the complete website
output = website.read()
# return the number of seconds passed since epoch
close_time = time()

#close the website
website.close()

#subtract and print the open time of the website from close time
print('The loading time of the website is',round(close_time-open_time,3),'seconds')
