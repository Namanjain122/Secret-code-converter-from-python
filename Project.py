from tkinter import *
from PIL import Image,ImageTk
def Secret_code():
    input_message = entry.get() #used to take input from user
    words = input_message.split(" ")
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "abc"
            r2 = "efg"
            new_string = r1 + word[1:] + word[0] + r2
            nwords.append(new_string)
        else:
            nwords.append(word[::-1])

    output_label.config(text=" ".join(nwords))  


#creating window
window = Tk()
window.geometry("1000x1000")
window.title("Secret code")

# Create input entry widget
entry_label = Label(window,text="Enter the message:",bg="red",fg="white")
entry_label.pack()
entry = Entry(window)
entry.pack()

convert_button = Button(window, text="Convert",bg="blue",fg="white",command=Secret_code)
convert_button.pack()

# Create output label widget
output_label = Label(window, text="")
output_label.pack()

# Start the tkinter event loop
window.mainloop()
