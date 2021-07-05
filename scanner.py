import scapy.all as scapy 
import speedtest
import socket
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
def scanfunc():
    global lst,label,str1
    request = scapy.ARP() 
      
    request.pdst = '192.168.0.0/24'
    broadcast = scapy.Ether() 
      
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
      
    request_broadcast = broadcast / request 
    clients = scapy.srp(request_broadcast, timeout = 1)[0] 
    lst=[]
    for element in clients: 
         lst.append(element[1].psrc + "      " + element[1].hwsrc)
 
    

    root = tkinter.Tk()
    root.title("SecTools")
    root.geometry("420x720")
    root.config(background="#343434")
    root.resizable(height = None, width = None)
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
        text="Scanning For Hosts Complete...",
        font=("Apple LiGothic", 25,"italic"),
        background="#343434",
        foreground="#00FFC9",
        

    )
    
    
    labeltext.pack(pady=(0, 15))


    
    
    for i in lst:
        k=i
        var=StringVar()
        var.set(k)
        label = Label(root, textvariable=var, relief=RAISED,bg="#343434",fg='#00FFC9' )
        label.config(height=2,width=150)
        label.pack()

  
    test = speedtest.Speedtest()
    down = test.download()/1000000
    upload = test.upload ()/1000000
    j=f"Download Speed: {down} Mbps"
    q=f"Upload Speed: {upload} Mbps"

    var2=StringVar()
    var2.set(j)
    label2 = Label(root, textvariable=var2, relief=RAISED,bg="#343434",fg='#00FFC9' )
    label2.config(height=2,width=150)
    label2.pack(pady=(40,0))

    var3=StringVar()
    var3.set(q)
    label3 = Label(root, textvariable=var3, relief=RAISED,bg="#343434",fg='#00FFC9' )
    label3.config(height=2,width=150)
    label3.pack()


    hostname = socket.gethostname()
    h=f"Hostname: {hostname}"
    m=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    ip=f"Your IP Address: {m}"

    var4=StringVar()
    var4.set(h)
    label4 = Label(root, textvariable=var4, relief=RAISED,bg="#343434",fg='#00FFC9' )
    label4.config(height=2,width=150)
    label4.pack()

    var5=StringVar()
    var5.set(ip)
    label5 = Label(root, textvariable=var5, relief=RAISED,bg="#343434",fg='#00FFC9' )
    label5.config(height=2,width=150)
    label5.pack()

    



    root.mainloop()
scanfunc()

