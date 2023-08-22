from tkinter import *
from  pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('Youtube video downloader')
link = StringVar()

Label(root, text='Youtube Video Downloader', font='arial 25 bold').pack()

Label(root, text='Paste Your Link here', font='arial 15 bold').place(x=160, y=70)

link_enter = Entry(root, width=70,textvariable=link).place(x=40, y=120)

def downloader():
    url = YouTube(str(link.get))
    video = url.streams.first()
    video.download()
    Label(root, text='Downloaded', font='arial 15 bold', bg='pale voilet red', padx=2, command = downloader).place(x=180,y=210)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = downloader).place(x=180 ,y = 150)

root.mainloop()
