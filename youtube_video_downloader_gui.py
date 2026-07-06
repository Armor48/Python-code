from pytube import Playlist
from tkinter import *
from tkinter import messagebox
import subprocess

# playlist_url = "https://youtu.be/-jKpGW4qD6A?si=R_kabbUl5FwH3d-h"

def download_playlist():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a playlist URL.")
        return

    try:
        subprocess.run([
            "yt-dlp",
            "-f", "bv*+ba/b",
            "--merge-output-format", "mp4",
            "--no-keep-video",
            "-o", "%(title)s.%(ext)s",
            url
        ], check=True)
        messagebox.showinfo("Download", f"Playlist downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Download", f"Error downloading playlist: {e}")

root = Tk()
root.title("YouTube Playlist Downloader")
root.geometry("500x200")
root.resizable(0, 0)
root.config(bg="black")

frame1 = Frame(root, bg="black")
name_label = Label(frame1, text="< YOUTUBE Video Downloader >",bg="red",fg= "white", font=("Arial", 18, "bold"),anchor="center")
name_label.pack(pady=(20,10))

frame2 = Frame(root, bg="black")
url_label = Label(frame2, text="Enter Video URL:", bg="black", fg="white", font=("Arial", 14, "bold"))
url_label.grid(row=0, column=0, padx=(20,10), pady=(10,10), sticky=W)
url_entry = Entry(frame2,width=30, fg="blue")
url_entry.grid(row=0, column=1, padx=(10,10), pady=(10,10), sticky=W)

frame3 = Frame(root, bg="black")
download_btn = Button(frame3, text="Download", bg="#EC250B", fg="#FFFFFF",command=download_playlist )
download_btn.pack()
download_btn.config(font=("verdana",12,"bold"))

frame1.pack()
frame2.pack()
frame3.pack()
root.mainloop()