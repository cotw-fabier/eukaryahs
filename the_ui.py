import tkinter as tk
import re
import pytube

def getTitle():
    yt = pytube.YouTube(youtubeURLString.get())
    return yt.title


pattern = re.compile("^(http(s)??\:\/\/)?(www\.)?((youtube\.com\/watch\?v=)|(youtu\.be\/))([a-zA-Z0-9\-_])+")


myWindow = tk.Tk()
myWindow.title("This is my first Python UI")

mainIntro = tk.Label(text="Youtube Video Downloader", font=('Roboto 25'), bg="#555555", fg="#ff0000")
mainIntro.pack()

secondaryIntro = tk.Label(text="Enter Your Video URL Here", font=('Roboto 20'))
secondaryIntro.pack()

youtubeURLString = tk.StringVar()
def youtubeURLCallback(event):
    if (pattern.match(youtubeURLString.get())):
        print("The pattern was matched!")
        videoTitle.config(text=getTitle())
    else:
        videoTitle.config(text="Please enter a valid Youtube URL")
    #print(youtubeURLString.get())
    return True

youtubeURL = tk.Entry(myWindow, textvariable=youtubeURLString)
youtubeURL.bind("<Return>", youtubeURLCallback)

youtubeURL.pack()


videoTitle = tk.Label(text="")
videoTitle.pack()

myWindow.mainloop()
