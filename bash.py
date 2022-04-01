# Author : Aank is ME
# -*- coding: utf-8 -*-
     
import os
import sys
import fileinput
          

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (success + "Done..")

   except KeyboardInterrupt:
       print (error + " Stopped!")
   except IOError:
       print (error + " File Not Found!")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (success + "Done..")
   except KeyboardInterrupt:
       print (error + " Stopped!")
   except IOError:
       print (error + " File Not Found!")


a2nkget = raw_input(W + "Choose" + G + " > ")

if a2nkget == "1" or a2nkget == "01":
   encrypt()
elif a2nkget == "2" or a2nkget == "02":
   decrypt()
else:
   print (eror + " Wrong input")
