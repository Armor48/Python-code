from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Gallery")
root.geometry("535x685")
root.resizable(0, 0)
root.configure(bg="black")
slideshow_running = False
    
def slideshow():
    global slideshow_running, slideshow_btn

    slideshow_running = not slideshow_running

    if slideshow_running:
        slideshow_btn.config(text="Stop Slideshow")
        loop_image(slideshow_running)
    else:
        slideshow_btn.config(text="Start Slideshow")
        root.after_cancel(loop_image)

def loop_image(cmd):
    global img_list, img_label

    if slideshow_running:
        img_list.append(img_list.pop(0)) 
        img_label.config(image=img_list[0])
        root.after(3000, loop_image, "slide")
    elif cmd == "next":
        img_list.append(img_list.pop(0)) #to move the first image in the list to the end of the list. this will create a loop effect when we click the next button.
        img_label.config(image=img_list[0]) #to update the image in the label to the first image in the list.
    elif cmd == "prev":
        img_list.insert(0, img_list.pop()) #to move the last image in the list to the beginning of the list. this will create a loop effect when we click the previous button.
        img_label.config(image=img_list[0]) #to update the image in the label to the first image in the list.
    else:
        root.after_cancel(loop_image) 

wallpaper_files = os.listdir("Image_folder") #to list all the files in the wallpapers directory. we can use this to get the names of the images in the directory.
img_list = [] #to store the images in a list. we will use this list to display the images in the window.
for file in wallpaper_files:
    img = Image.open(f"Image_folder/{file}") #to open each image file in the wallpapers directory.
    resized_img = img.resize((500, 500)) #to resize the image to fit the window.
    img_list.append(ImageTk.PhotoImage(resized_img)) #to convert the image to a format that can be used in tkinter and add it to the list.
img_label = Label(root,image=img_list[0]) #to create a label to display the images. we will update the image in this label to create a slideshow effect.
img_label.grid(row=0, column=0, columnspan=2, padx=15, pady=20) #to position the image label in the window using grid. we will place it in the first row and span across 2 columns.

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

prev_btn = Button(frame1, text = "Previous", bg="#23AFAA", fg="white", width=17, height=1,command=lambda: loop_image("prev"))
prev_btn.pack(fill=X)  
prev_btn.config(cursor="hand2",font=("Arial", 18,"bold"))

next_btn = Button(frame2, text = "Next", bg="#23AFAA", fg="white", width=17, height=1,command=lambda: loop_image("next"))
next_btn.pack(fill=X)   
next_btn.config(cursor="hand2",font=("Arial", 18,"bold"))

slideshow_btn = Button(frame3, text = "Start Slideshow", bg="#23AFAA", fg="white", width=35, height=1,command=slideshow)
slideshow_btn.pack()  
slideshow_btn.config(cursor="hand2",font=("Arial", 18,"bold"))

frame1.grid(row=1, column=0)
frame2.grid(row=1, column=1)
frame3.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()