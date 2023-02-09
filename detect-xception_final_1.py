
import tensorflow as tf

import os
import numpy as np

import cv2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog 

model_path = "model_inception.h5"
loaded_model = tf.keras.models.load_model(model_path)
def fun(a,b):
    s=0
    image = a#cv2.imread("p (11).jpg")
    print(image.shape)

    r_image = cv2.resize(image,(200,200)) 
    input_data = np.array([r_image])
    print(input_data.shape)
    input_data = input_data/255

    pred = loaded_model.predict(input_data)
    result = np.argmax(pred)
    print(result)

    if result==1:
        
         print("meningioma_tumor    ");
         s= "meningioma_tumor                 " 
         Label(login_screen, text="Result:"+"  "+s+'',bg="blue", font=("Calibri", 30)).place(x=100,y=300)
  
    if result==3:
        
         print("pituitary_tumor");
         s= "pituitary_tumor    " 
         Label(login_screen, text="Result:"+"  "+s+'',bg="blue", font=("Calibri", 30)).place(x=100,y=300)
    if result==2:
        
         print("No brain Tumour");
         s= "NO Brain tumor  " 
         Label(login_screen, text="Result:"+"  "+s+'',bg="blue", font=("Calibri", 30)).place(x=100,y=300)
    if result==0:
        
         print("glioma Tumor");
         s= "Glioma Tumor   " 
         Label(login_screen, text="Result:"+"  "+s+'',bg="blue", font=("Calibri", 30)).place(x=100,y=300)
def open_file():
    img=0
    filename = filedialog.askopenfilename(title ='"pen')
    print( filename)
    if filename.endswith(".jpg"):
        img = cv2.imread(filename)
        #image_resized = img.resize(img, (128, 128))
        print(img)
        print(filename)
        fun(img,filename)

def login():
    global login_screen
    login_screen = Tk()
    login_screen.title("Brain Tumor Detection")
    login_screen.geometry("766x708")
    login_screen.configure(background='white')
    Label(login_screen, text="   Brain Tumour Detection ",bg="blue", font=("Calibri", 30)).place(x=150,y=10)
    Label(login_screen, text="   ",bg="blue", font=("Calibri", 30)).place(x=150,y=10)
    Button(login_screen, text="select image", width=30, height=5,bd=5, command =open_file,bg="blue",activebackground="#c6eb73").place(x=300,y=600)
    login_screen.mainloop()
login()
