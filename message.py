from tkinter import *
import base64
import sys


class messageEd:
    
    def __init__(self):
        
        # initialising
        self.window = Tk()
        self.window.geometry('500x300')
        self.window.resizable(0, 0)
        self.window.title("Encode and Decode Messages")
        self.stored_text = StringVar()
        self.private_key = StringVar()
        self.choice = StringVar()
        self.user_input = StringVar()
        self.result = StringVar()
        self.build()

    def build(self):

        Label(self.window, text='ENCODE DECODE', font='arial 20 bold').pack()

        # create label and entry for message input
        Label(self.window, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
        Entry(self.window, font='arial 10', textvariable=self.stored_text, bg='ghost white').place(x=290, y=60)

        # create label and entry for common key for encoding and decoding
        Label(self.window, font='arial 12 bold', text='KEY').place(x=60, y=90)
        Entry(self.window, font='arial 10', textvariable=self.private_key, bg='ghost white').place(x=290, y=90)

        # create label and buttons for mode, either endoe or decode
        Label(self.window, font='arial 12 bold', text='MODE').place(x=60, y=120)
        Button(self.window, font='arial 10', text='Encode', padx=1.5, bg='LightGray', command=lambda: self.user_choice('encode')).place(x=290, y=120)
        Button(self.window, font='arial 10', text='Decode', padx=1.5, bg='LightGray', command=lambda:self.user_choice('decode')).place(x=370, y=120)
        
        # create label and entry for output result
        Label(self.window, font='arial 12 bold', text='RESULT').place(x=60, y=150)
        Entry(self.window, font='arial 10 bold', textvariable= self.result, bg='ghost white').place(x=290, y=150)

        # create buttons to reset all fields or exit program
        Button(self.window, font='arial 10 bold', text='RESET', width=6, command=self.reset, bg='LimeGreen', padx=2).place(x=80, y=190)
        Button(self.window, font='arial 10 bold', text='EXIT', width=6, command= self.exit, bg='OrangeRed', padx=2, pady=2).place(x=180, y=190)

        self.window.mainloop()
        
    def encoder(self, key, message):
        self.encode_list = []
        for i in range(len(message)):
            key_c = key[i % len(key)]
            self.encode_list.append(chr((ord(message[i]) + ord(key_c)) % 256))
        return base64.urlsafe_b64encode("".join(self.encode_list).encode()).decode()

    def decoder(self, key, message):
        self.decode_list = []
        message = base64.urlsafe_b64decode(message).decode()
        for i in range(len(message)):
            key_c = key[i % len(key)]
            self.decode_list.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
        return "".join(self.decode_list)

    # to set mode as either encode or decode based on user input
    def user_choice(self, input_type):
        self.user_input.set(input_type)
        self.mode()

    def mode(self):
        self.choice = self.user_input.get()
        if (self.choice == 'encode'):
            self.result.set(self.encoder(self.private_key.get(), self.stored_text.get()))
        elif (self.choice == 'decode'):
            self.result.set(self.decoder(self.private_key.get(), self.stored_text.get()))

    def exit(self):
        sys.exit()

    def reset(self):
        self.stored_text.set("")
        self.private_key.set("")
        self.result.set("")


messageEd()
