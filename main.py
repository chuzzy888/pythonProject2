from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

class YouTubeDownloader(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Video URL entry field
        self.url_label = tk.Label(self, text="welcome to CHIZTUBE APPLICATION Enter YouTube video URL:", bg="white", fg="black")
        self.url_label.pack(side="top")
        self.url_entry = tk.Entry(self, bg="light gray", fg="black")
        self.url_entry.pack(side="top")

        # Download location button and label
        self.path_label = tk.Label(self, text="Choose download location:", bg="white", fg="RED")
        self.path_label.pack(side="top")
        self.path_button = tk.Button(self, text="Browse...", command=self.choose_path, bg="gray", fg="white")
        self.path_button.pack(side="top")
        self.path_var = tk.StringVar()
        self.path_var.set("Current directory")
        self.path_display = tk.Label(self, textvariable=self.path_var, bg="white", fg="RED")
        self.path_display.pack(side="top")

        # Download button
        self.download_button = tk.Button(self, text="Download", command=self.download, bg="GREY", fg="white")
        self.download_button.pack(side="bottom")

    def choose_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)

    def download(self):
        # Get video URL and download path from the GUI
        url = self.url_entry.get()
        path = self.path_var.get()

        # Create a YouTube object and get the video stream with the highest resolution
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print("Downloading...")
        stream.download(path)
        print("Download completed!")

root = tk.Tk()
root.configure(bg="white")
app = YouTubeDownloader(master=root)
app.mainloop()

