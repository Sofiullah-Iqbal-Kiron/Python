# YouDowr: the youtube video downloader.
# Just put watch link below, the video will be downloaded for you in desired path.
# Use OOP to construct individual objects.

from tkinter import *
from pytube import *
from tkinter import filedialog


class AppWindow(Tk):
    pass


class Prompt(Label):
    pass


class InsertLink(Entry):
    pass


class Download(Button):
    pass


class AvailableVideoCodec(OptionMenu):
    pass


# class ChoosePathToSaveVideo(filedialog):
#     pass


root = AppWindow()
root.title("YouDowr")
ent = Entry(root, width=20, bg='gray')
ent.pack()


def downVideo():
    video = YouTube(ent.get().strip())
    video.streams.first().download()


Button(root, text="Download", padx=20, pady=9, command=downVideo).pack()

root.mainloop()
