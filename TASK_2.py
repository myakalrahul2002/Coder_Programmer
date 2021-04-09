from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry('350x200')
root.title('CODERPROGRAMER - TEXT_TO_SPEECH')

Label(root, text = 'TEXT-TO-SPEECH').pack()
Label(root, text ='CODERPROGRAM').pack(side="bottom")

Label(root, text ='Enter Text').place(x=20,y=60)

msg = StringVar()

entry_field = Entry(root,textvariable = msg, width ='50')
entry_field.place(x=20 , y=80)

def texttospeech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('CODERPROGRAM.mp3')
    playsound('CODERPROGRAM.mp3')

def exit():
    root.destroy()

def reset():
    Msg.set("")

Button(root, text = "Play" ,  command =texttospeech, width =4).place(x=25, y=120)
Button(root,text = 'Exit',command = exit).place(x=100,y=120)
Button(root, text = 'Reset', command = reset).place(x=175 , y =120)

root.mainloop()
