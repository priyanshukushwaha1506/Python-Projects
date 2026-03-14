import time
import tkinter as tk
from PIL import Image, ImageTk
#Main Application Window
root=tk.Tk()
root.title('SlideShow')
root.geometry("900x900")
#list of images
image_paths= [
r"F:\OneDrive\Pictures\IMG_20250809_122817.jpg",
r"F:\OneDrive\Pictures\IMG_20250809_115409.jpg",
r"F:\OneDrive\Pictures\WhatsApp Image 2025-09-30 at 14.17.42_644bc133.jpg",
r"F:\OneDrive\Pictures\WhatsApp Image 2025-09-30 at 14.17.41_88dd2bee.jpg",
r"F:\OneDrive\Pictures\IMG_20250809_131102.jpg",
r"F:\OneDrive\Pictures\IMG_20250908_182827.jpg",
r"F:\OneDrive\Pictures\Untitled\IMG-20250315-WA0017.jpg",
r"F:\OneDrive\Pictures\Untitled\IMG-20250315-WA0035.jpg",
r"F:\OneDrive\Pictures\Untitled\SAVE_20250317_152236.jpg",
r"F:\OneDrive\Pictures\Untitled\Screenshot_2025-01-27-04-12-40-809_com.google.android.youtube.jpg",
r"F:\OneDrive\Pictures\Untitled\WhatsApp Image 2025-07-29 at 09.36.31_a599b855.jpg",
r"F:\OneDrive\Pictures\Untitled\WhatsApp Image 2025-07-29 at 09.36.31_a599b855.jpg",
r"F:\OneDrive\Pictures\Untitled\ram - Copy (2).jpg",
r"F:\OneDrive\Pictures\Untitled\IMG20210623161020_01.jpg",
r"F:\OneDrive\Pictures\Untitled\IMG20230903082133.jpg",
]   
image_size=(800,800)
images=[]
for path in image_paths:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img)

# Convert Pil images into Tkinteer Compatible Image
final_images=[]
for img in images:
    photo=ImageTk.PhotoImage(img)
    final_images.append(photo)
#image label widget to keep photo
image_label=tk.Label(root)    
image_label.pack(pady=30)
def start_slideshow():
 for photo in final_images:
   image_label.config(image=photo)
   image_label.image=photo
   root.update()
   time.sleep(2)
#Button
play_button=tk.Button(
  root,
  text="Play The Slideshow",
  font={'Orange',17},
  command=start_slideshow
)
play_button.pack(pady=50)
root.mainloop()