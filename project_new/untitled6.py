# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 08:00:22 2020

@author: hp
"""
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import random
import base64
import os
import smtplib
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

root2=Tk()
root2.title("Encrypt/Decrypt Messaging")

encryptedfile=[]
unencryptedfile=[]

topemail=Frame(root2)
topemail.pack(side="top",fill="both",expand=True)
midemail=Frame(root2)
midemail.pack(side="top",fill="both")
downemail=Frame(root2)
downemail.pack(side="top",fill="both",expand=True)
sdownemail=Frame(root2)
sdownemail.pack(side="top",fill="both",expand=True)

label1000=Label(topemail,text="Encrypt/Decrypt E-mail Messaging")
label1000.config(font=("Courier",40))
label1000.pack(fill="both")

main_frameemail=Frame(topemail,padx=5,pady=5)
main_frameemail.pack(fill="both",expand=True)

label800=Label(main_frameemail,text="                                       Enter Secret Key (only integar): ")
label800.config(font=("Courier",15))
label800.pack(side="left")

userkeyemail=Entry(main_frameemail,width=22)
userkeyemail.insert(0,1)
userkeyemail.pack(side="left",ipady=5)


def askfilenameemail(abc):
    label104.pack_forget()
    file_path=filedialog.askopenfilename()
    abc.insert(END,file_path)
    abc.insert(END,",")




lnframeemail=Frame(topemail,padx=40,pady=15)
lnframeemail.pack(side="top",fill="both",expand=True)

label500email=Label(lnframeemail,text="Attach files to be encrypted: ")
label500email.config(font=("Courier",15))
label500email.pack(side="left")

file=Entry(lnframeemail,width=30)
file.pack(side="left",ipady=10)

label501=Label(lnframeemail,text="  ")
label501.config(font=("Courier",15))
label501.pack(side="left")

next1_buttonemail=Button(lnframeemail,text="Browse",padx=5,pady=3,font=50,command=lambda: askfilenameemail(file))
next1_buttonemail.pack(side="left")


label502=Label(lnframeemail,text=" Attach original files: ")
label502.config(font=("Courier",15))
label502.pack(side="left")

orifile=Entry(lnframeemail,width=30)
orifile.pack(side="left",ipady=10)

label601=Label(lnframeemail,text="  ")
label601.config(font=("Courier",15))
label601.pack(side="left")

next2_buttonemail=Button(lnframeemail,text="Browse",padx=5,pady=3,font=50,command=lambda: askfilenameemail(orifile))
next2_buttonemail.pack(side="left")

label102=Label(lnframeemail,text="  ")
label102.config(font=("Courier",15))
label102.pack(side="left")

label103=Label(lnframeemail,text="Status: ")
label103.config(font=("Courier",15))
label103.pack(side="left")

label104=Label(lnframeemail,text="Done")
label104.config(font=("Courier",15))
label104.pack(side="left")

label104.pack_forget()








left_frame=Frame(topemail,bg="black",padx=35,pady=15)
left_frame.pack(side="left",fill="both",expand=True)
right_frame=Frame(topemail,bg="black",padx=35,pady=15)
right_frame.pack(side="left",fill="both",expand=True)


label1111=Label(left_frame,text="Input Text",font=100)
label2111=Label(right_frame,text="Output Text",font=100)
inputtextemail=scrolledtext.ScrolledText(left_frame,bg="white")
outputtextemail=scrolledtext.ScrolledText(right_frame,bg="white")
label1111.pack(fill="both")
label2111.pack(fill="both")
inputtextemail.pack(fill="both",expand=True)
outputtextemail.pack(fill="both",expand=True)

new_left=Frame(midemail,bg="grey")
new_left.pack(side="left",fill="both",expand=True)
new_right=Frame(midemail,bg="grey")
new_right.pack(side="right",fill="both",expand=True)



def Resetallemail():
    inputtextemail.delete('1.0',END)
    outputtextemail.delete('1.0',END)
    userkeyemail.delete(0,'end')
    useremail.delete(0,'end')
    userpass.delete(0,'end')
    destemail.delete(0,'end')
    userkeyemail.insert(0,1)

def Resetemail():
    outputtextemail.delete('1.0',END)


def Encriptingemail():
    keyy=int(userkeyemail.get())
    files=file.get().split(',')
    for i in files:
        if(not(i=='')):
            fl=open(i,"rb")
            data=fl.read()
            fl.close()
            
            data= bytearray(data)
            for index, value in enumerate(data):
                data[index]=value^keyy
                
            naming=i.split('/')
            k=len(naming)
            i=naming[k-1]
            
            newabhistr="Encrypted-"+i
            encryptedfile.append(newabhistr)
            
            fle=open("Encrypted-"+i,"wb")
            fle.write(data)
            fle.close
            label104.pack(side="left")

    
    itxt=inputtextemail.get("1.0",END)
    key=userkeyemail.get()
    enc=[]
    for i in range(len(itxt)):
        key_c=key[i%len(key)]
        enc_c=chr(ord(itxt[i])+
                  ord(key_c)%256)
        enc.append(enc_c)
    otxt=base64.urlsafe_b64encode("".join(enc).encode()).decode()
    
    outputtextemail.insert(END,otxt)
    outputtextemail.insert(END,"\n\n")
    
            
def Decriptingemail():
    itxt=inputtextemail.get("1.0",END)
    key=userkeyemail.get()
    dec=[]
    itxt=base64.urlsafe_b64decode(itxt).decode()
    for i in range(len(itxt)):
        key_c=key[i%len(key)]
        dec_c=chr((256+ord(itxt[i])-ord(key_c))%256)
        dec.append(dec_c)
    otxt="".join(dec)
    outputtextemail.insert(END,otxt)
    outputtextemail.insert(END,"\n\n")

def Sendingmails():
    files=orifile.get().split(',')
    for i in files:        
        newabhistr=i
        unencryptedfile.append(newabhistr)
    
    encryptedfile.extend(unencryptedfile)
    
    
    try:
            loginmail=useremail.get()
            loginpassword=userpass.get()
            destinations=destemail.get().split(',')
            txt=outputtextemail.get("1.0",END)
            leng=len(txt)
            if(loginmail=="" or loginpassword=="" or destinations==[''] or leng==0):
                messagebox.showerror("Error","All fields in email are required")
            
            smtp_server = "smtp.gmail.com"
            smtp_port = 587                                 # for smtp.gmail.com
            from_address = loginmail             # e.g. username@gmail.com
            from_password = loginpassword    # required by script to login using your username
            to_address = destinations                # e.g. username2@gmail.com
            subject = "Message from someone whom you might know"               
            mail_body = txt
            
            files=encryptedfile
            del files[-1]
            print(destinations)
            print(files)
 
            msg = MIMEMultipart()
            msg['Subject'] =  subject
            msg['To'] = str(to_address)
            msg.attach(MIMEText(mail_body))
 
            for file in files:
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(file, "rb").read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
                msg.attach(part)
 
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_address, from_password)
            server.sendmail(from_address, to_address, msg.as_string())
            print("all done")
            messagebox.showinfo("Message sent","E-mail sent to destinations")
            server.quit()
    except:
            messagebox.showerror("Error","Unable to send mail...check your internet connection")

btnenc=Button(new_left,text="Encrypt",bg="white",padx=20,pady=15,font=90,command=Encriptingemail)
btndec=Button(new_left,text="Decrypt",bg="white",padx=20,pady=15,font=90,command=Decriptingemail)
btnreset=Button(new_right,text="Reset Output",bg="white",padx=20,pady=15,font=90,command=Resetemail)
btnexit=Button(new_right,text="Reset All",bg="white",padx=20,pady=15,font=90,command=Resetallemail)

btnenc.pack(side="left",fill="both",expand=True)
btndec.pack(side="left",fill="both",expand=True)
btnreset.pack(side="left",fill="both",expand=True)
btnexit.pack(side="left",fill="both",expand=True)

label6=Label(downemail,text="Send E-Mail",padx=10)
label6.config(font=("Courier",18))
label6.pack(fill="both")

label3=Label(downemail,text="(Output text will be sent)",padx=10)
label3.config(font=("Courier",10))
label3.pack(fill="both")

label5=Label(downemail,text="Enter your email: ",padx=10)
label5.config(font=("Courier",13))
label5.pack(side="left",fill="both")

useremail=Entry(downemail,width=40)
useremail.pack(side="left",ipady=5)

label4=Label(downemail,text="Enter your password: ",padx=10)
label4.config(font=("Courier",13))
label4.pack(side="left",fill="both")

userpass=Entry(downemail,width=22,show="*")
userpass.pack(side="left",ipady=5)

label7=Label(downemail,text="Enter your destination Email: ",padx=10)
label7.config(font=("Courier",13))
label7.pack(side="left",fill="both")

destemail=Entry(downemail,width=40)
destemail.pack(side="left",ipady=5)

btnsend=Button(downemail,text="Send",font=("Courier",13),command=Sendingmails)
btnsend.pack(expand=True)

label9=Label(sdownemail,text="              ",padx=10)
label9.config(font=("Courier",13))
label9.pack(fill="both")
root2.state('zoomed')
root2.mainloop()