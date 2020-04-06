# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:26:31 2020

@author: Hemraj
"""
import random
import smtplib
import tkinter as tk
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def CreateWidget():
    emailLabel = Label(win,text="Enter your Email Id : ",bg='deepskyblue3')
    emailLabel.grid(row=0,column=1,padx=5,pady=5)
    
    emailEntry = Entry(win,textvariable=emailid, width = 30)
    emailEntry.grid(row=0,column=2,padx=5,pady=5)
    
    sendOTPbutton = Button(win,text="Send OTP",command=sendOTP, width=20)
    sendOTPbutton.grid(row=0,column=3,padx=5,pady=5)
    
    win.msgLabel = Label(win,bg="deepskyblue3")
    win.msgLabel.grid(row=1,column=1,padx=5,pady=5,columnspan=3)
    
    otpLabel = Label(win,text="Enter the OTP : ",bg="deepskyblue3")
    otpLabel.grid(row=2,column=1,padx=5,pady=5)
    
    win.otpEntry=Entry(win,textvariable=otp,width=30 ,show='*')
    win.otpEntry.grid(row=2,column=2,padx=5,pady=5)
    
    validOTPbutton=Button(win,text='Validate OTP',command=validOTP,width=20)
    validOTPbutton.grid(row=2,column=3,padx=5,pady=5)
    
    win.otpLabel=Label(win,bg="deepskyblue3")
    win.otpLabel.grid(row=3,column=1,padx=5,pady=5,columnspan=3)
    
def sendOTP():
    numbers='0123456789'
    win.genOTP=""
    receiverEmail=emailid.get()
    
    for i in range(5):
        win.genOTP += numbers[int(random.random() * 10)]
    otpMSG= "YOUR OTP IS : " + win.genOTP
        
    message=MIMEMultipart()
    message['FROM'] = "OTP VERIFICATION (google)"
    message['To']= receiverEmail
    message["Subject"] ='OTP VERIFICATION'
    message.attach(MIMEText(otpMSG))
    
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()
    
    smtp.login('skybluecompany18@gmail.com', 'papa@123')
    
    smtp.sendmail('skybluecompany18@gmail.com',receiverEmail,message.as_string())
    
    smtp.quit()
    
    
    receiverEmail='{}**********{}'.format(receiverEmail[0:2],receiverEmail[-10:])
    
    win.msgLabel.config(text="OTP HAS BEEN SEND TO " + receiverEmail)
    

def validOTP():
    userInputOTO=otp.get()
    systemOTP=win.genOTP
    
    
    
    if userInputOTP==systemOTP:
        win.otpLabel.config(text="OTP VALIDATE SUCCESSFULLY")
    else:
        win.otpLabel.config(text="INVALID OTP")
    
    
    
    
    
win=Tk()
win.title("Email OTP")
#win.resizable(False,False)
win.config(bg='deepskyblue3')
emailid=StringVar()
otp=StringVar()

CreateWidget()

win.mainloop()