import datetime 
import os
import sys
import fileIO
import subprocess

#passed args
fileFormatting = sys.argv[1]
fileName = sys.argv[2]


#config stuff
#fileFormatting = fileIO.fileLoad("./config.json")["fileFormatting"]
key = fileIO.fileLoad("./config.json")["key"]
url = fileIO.fileLoad("./config.json")["url"]

def formatter(file,fileName):
    name=file
    date = datetime.datetime.now()
    name = name.replace("%Time%",date.strftime("%H-%M-%S"))
    name = name.replace("%Date%",date.strftime("%d_%m_%d"))
    name = name.replace("%File%",os.path.basename(fileName))
    print(name)
    return name

	#%h:%mi:%s-%d.%mo.%yy"



def curlUploader(file,fileName,key,uploadURL):
    string = 'curl -F "name={0}" -F "key={1}" -F "d=@{2}" {3}'.format(file,key,fileName,uploadURL)
    a = subprocess.check_output(string, shell=True) #moves file 
    return a.decode()

def addToClipboard(clipboard):
    #print(clipboard)
    string = "echo -n " + clipboard + " | xclip -selection clipboard"
    print(string)
    subprocess.call(string, shell=True)

def notification(notification):
    subprocess.call("notify-send {0}".format(notification), shell=True)


	
print(fileName)
name = formatter(fileFormatting,fileName)
returnURL = curlUploader(name,fileName,key,url)
notification("Image uploaded to {0}".format(returnURL))
print(returnURL)
addToClipboard(returnURL)
