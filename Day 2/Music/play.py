import tkinter as tk
from pygame import mixer
import urllib.request
from io import BytesIO
from mutagen.mp3 import MP3

music_url = "https://firebasestorage.googleapis.com/v0/b/ws-test-71d81.appspot.com/o/music%2FThe%20Chainsmokers%20-%20Closer%20ft.%20Halsey.mp3?alt=media&token=e742a444-27dd-4f3d-8cac-0f28e6f9b811"
player = None

def get_audio_from_url(trackUrl):
    req = urllib.request.Request(trackUrl)
    resp = urllib.request.urlopen(req)
    byteAudio = BytesIO(resp.read())
    return byteAudio

def load_music():
    global music_url
    global player
    player = mixer
    player.init()
    player.music.load(get_audio_from_url(music_url))
    player.music.set_volume(1)
    player.music.play()

def stop():
    global player
    if player.music.get_busy():
            player.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Music")
    root.state("zoomed")
    button = tk.Button(text="Play", command=load_music)
    pause = tk.Button(text="Stop", command=stop)

    button.grid(row=0, column=0, padx=10, sticky=tk.E)
    pause.grid(row=0, column=1, padx=10, sticky=tk.W)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure((0,1), weight=1)

    root.mainloop()
