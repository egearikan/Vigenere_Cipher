from tkinter import *
import string
root=Tk()
root.geometry("500x700")

topFrame=Frame(root)
topFrame.pack()

KeyBox=Entry(topFrame,width=40)
KeyBox.pack()

MessageBox=Text(topFrame, height=15, width=50)
MessageBox.pack()
ResultBox=Text(topFrame, height=15, width=50)
ResultBox.pack()
key=''

def encryption():
 
    ResultBox.delete('1.0', END)
    ResultBox.update()
    global key
    key=KeyBox.get()
    if key == '':
        key='EGE'

    key=key.upper()
    message=MessageBox.get("1.0","end-1c")
    message=message.replace(' ','')
    message=message.upper()
    
    message=message.translate(str.maketrans('', '', string.punctuation))
    message=message.replace('\n', '')
    message=message.replace('\r', '')
    res=int()
    chiperText=''

    for i in range(len(message)):
        b=message[i]
        
        if b.isalpha():
            a=i%len(key)

            if key[a] == ' ':
                if message[i]!='A':
                    res=ord(message[i])-1
                    chiperText+=chr(res)
                else:
                    continue
            else:
                res=(ord(message[i])+ord(key[a])) %26
                res+=ord('A')
                chiperText+=chr(res)
        elif b.isdigit():
            #mod 9
            chiperText+= str((int(b)+len(key))%10)        
        else:
            continue

    ResultBox.insert(END,chiperText)

    


def decryption():

    global key
    ResultBox.delete('1.0', END)
    ResultBox.update()
    global key
    key=KeyBox.get()
    if key == '':
        key='EGE'

    key=key.upper()
    message=MessageBox.get("1.0","end-1c")
    message=message.upper()
    res=''
    originalText=''
    a=0
    for i in range(len(message)):
        b=message[i]

        if b.isalpha():
            a=i%len(key)
            #boşluk casei ?
            
            if key[a] == ' ':
                if message[i]!='A':
                    res=ord(message[i])+1
                    originalText+=chr(res)
                else:
                    continue
            else :
                res=(ord(message[i])-ord(key[a])) %26
                res+=ord('A')
                originalText+=chr(res)
        elif b.isdigit():
            originalText+=str((int(b)-len(key)+10)%10)
        else:
            continue
    
    ResultBox.insert(END,originalText)
    


EncButton=Button(topFrame,height=1, width=15, text="Encrypt", command=lambda: encryption())
EncButton.pack(side=LEFT)
DecButton=Button(topFrame,height=1, width=15, text="Decrypt", command=lambda: decryption())
DecButton.pack(side=LEFT)


mainloop()