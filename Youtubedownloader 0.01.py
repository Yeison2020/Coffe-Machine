# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 00:26:43 2020

@author: Yeison Casado

"""
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Best option in market")


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()


# Enter link

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_Enter = Entry(root, width = 70, textvariable = link).place(x=32, y=90)


#Funtion to download

def Downloader():
    
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = "DOWNDlOADED", font = 'arial 15').place(x=180,y=210)
    
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)    
    
    
root.mainloop()    