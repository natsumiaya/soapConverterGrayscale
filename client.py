#!/usr/bin/env python

from suds.client import Client
import Image
import base64
import StringIO
import thread
import time
import os
'''
client = Client('http://localhost:8080/Convert/soap/description')
'''
files1=[]
files2=[]
files3=[]

path="F:/My Documents/SEMESTER 6/SISTER/dataset2/"
destpath="F:/My Documents/SEMESTER 6/SISTER/dataset_grayscale/"
dirs = os.listdir(path)
i=0
for file in dirs:
    if ".png" in file or ".jpg" in file:
        if i%3==0:
            files1.append(file)
        elif i%3==1:
            files2.append(file)
        else:
            files3.append(file)
        i=i+1

#def kirimgambar( listGambar, server ):
    #client = Client('http://'+server+'/Convert/soap/description')
def kirimgambar( listGambar ):
    client = Client('http://localhost:8080/Convert/soap/description')
    
    for file in listGambar:
        fullpath=path+file
        files = open(fullpath,'rb')
        bytes = bytearray(files.read())
        convert = base64.b64encode(bytes)
        files.close()
        
        binary=client.service.grayscale(convert)
        f = open(destpath+file, 'wb')
        ba = bytearray(base64.b64decode(binary))
        f.write(ba)
        f.close()
        print "done ",file

# Create two threads as follows
try:
   thread.start_new_thread( kirimgambar, (files1, ) )
   thread.start_new_thread( kirimgambar, (files2, ) )
   thread.start_new_thread( kirimgambar, (files3, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass

