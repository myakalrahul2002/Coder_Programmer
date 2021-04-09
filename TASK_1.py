from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(0,0)

root.title("CODERPROGRAM-Message Encode and Decode")
Label(root, text ='ENCODE DECODE').pack()
Label(root, text ='CODERPROGRAM').pack(side =BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

"FUNCTION OF ENCODE"
def Eencode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

"FUNCTION OF DECODE"
def Ddecode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

"FUNCTION OF SET MODE"
def Mmode():
    if(mode.get() == 'e'):
        Result.set(Eencode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Ddecode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

"FUNCTION OF EXIT"
def Eexit():
    root.destroy()

"FUNCTION OF RESET"
def Rreset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

#Message
Label(root, text='MESSAGE').place(x= 60,y=60)
Entry(root, textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

#key
Label(root, text ='KEY').place(x=60, y = 90)
Entry(root,  textvariable = private_key , bg ='ghost white').place(x=290, y = 90)


#mode
Label(root, text ='MODE(e,E-encode, d-decode)').place(x=60, y =120)
Entry(root, textvariable = mode , bg= 'ghost white').place(x=290, y = 120)


#result
Entry(root, textvariable = Result, bg ='ghost white').place(x=290, y = 150)


######result button
Button(root, text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mmode).place(x=60, y = 150)


#reset button
Button(root,text ='RESET' ,width =6, command = Rreset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

#exit button
Button(root ,text= 'EXIT' , width = 6, command = Eexit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

root.mainloop()

