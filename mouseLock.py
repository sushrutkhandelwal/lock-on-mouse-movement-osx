import autopy
import os
import time
import datetime 
#sudo pip install autopy
autopy.mouse.move(0,0)
time.sleep(5)

x,y=autopy.mouse.get_pos()
while(x<20 and y<20):
	x,y=autopy.mouse.get_pos()

name=datetime.datetime.now().strftime("%d%B%I_%M%p")
#brew install imagesnap
os.system("imagesnap -w 1 "+name+".jpg")
os.system("pmset displaysleepnow")