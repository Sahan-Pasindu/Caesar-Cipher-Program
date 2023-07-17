from tkinter import *


def main_screen():
    screen = Tk()
    screen.geometry("400x500")

    screen.title("Caesar Cipher Application")

    def encrypt():
        letters = 'abcdefghijklmnopqrstuvwxyz'
        num_letters = len(letters)
        key = int(text1.get(1.0, END))
        text = text2.get(1.0, END)
        result = ''

        for letter in text:
            letter = letter.lower()
            if not letter == ' ':
                index = letters.find(letter)
                if index == -1:
                    result += letter
                else:
                    new_index = index + key
                    if new_index >= num_letters:
                        new_index -= num_letters
                    elif new_index < 0:
                        new_index += num_letters
                    result += letters[new_index]

        text3.delete(1.0, END)
        text3.insert(END, result)

    def decrypt():
        letters = 'abcdefghijklmnopqrstuvwxyz'
        num_letters = len(letters)
        key = int(text1.get(1.0, END))
        text = text2.get(1.0, END)
        result = ''

        for letter in text:
            letter = letter.lower()
            if not letter == ' ':
                index = letters.find(letter)
                if index == -1:
                    result += letter
                else:
                    new_index = index - key
                    if new_index >= num_letters:
                        new_index -= num_letters
                    elif new_index < 0:
                        new_index += num_letters
                    result += letters[new_index]

        text3.delete(1.0, END)
        text3.insert(END, result)

    def reset():
        # text1.delete(1.0, END)
        text2.delete(1.0, END)
        text3.delete(1.0, END)

    Label(text="Caesar Cipher Application", fg="black", font=("calbri", 18)).place(x=50, y=10)

    Label(text="Enter the key:", fg="black", font=("calbri", 13)).place(x=30, y=50)
    text1 = Text(font="Roboto 13", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=145, y=50, width=50, height=25)

    Label(text="Enter the text to Encrypt/Decrypt:", fg="black", font=("calbri", 13)).place(x=30, y=80)
    text2 = Text(font="Roboto 13", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=25, y=110, width=350, height=100)

    Button(text="Encrypt", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=30, y=220)
    Button(text="Decrypt", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=220)
    Button(text="Reset", height="2", width=47, bg="#1089ff", fg="white", bd=0, command=reset).place(x=30, y=260)

    text3 = Text(font="Roboto 13", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text3.place(x=25, y=310, width=350, height=150)

    screen.mainloop()


main_screen()
