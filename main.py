from pytesseract import pytesseract #pytesseract
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import PIL.Image


window = tk.Tk() #makes window  
window.title("math") #window title

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #path to pytesseract this will change for mac users :(
pytesseract.tesseract_cmd = path_to_tesseract

file_path = filedialog.askopenfilename()
print(file_path)


img = PIL.Image.open(file_path)
text = pytesseract.image_to_string(img)  # converts text to string

label_output = tk.Label(text=eval(text), font=('Times', 40))
label_output.grid()

window.deiconify()
window.mainloop()
