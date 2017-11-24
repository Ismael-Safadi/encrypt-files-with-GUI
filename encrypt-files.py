from tkinter import*
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from Crypto.Cipher import XOR
import base64
from tkinter import messagebox
root = Tk()
root.iconbitmap('tends.ico')
root.title("Encryption and Decryption Tool'TENDS TEAM'")
def filename():
    global path
    path = askopenfilename()
    return path
    
    
    

def onc(filename):
    key=Name.get()
    print key
    
    print path
    if var.get() == 1:
        chipher = XOR.new(key)
        file = open(path, 'r')
        read = file.read()
        file.close()
        new = base64.b64encode(chipher.encrypt(read))
        newfile = open(path, 'w')
        read = newfile.write(new)
        newfile.close
    elif var.get() ==2:
        chipher = XOR.new(key)
        file = open(path, 'r')
        read = file.read()
        file.close()
        new = chipher.decrypt(base64.b64decode(read))
        newfile = open(path, 'w')
        read = newfile.write(new)
        newfile.close()
    messagebox.showinfo(title="Done", message="Done ^__^ Your file is secure ")    
var = IntVar()
ttk.Radiobutton(root, text="encrypt", variable=var, value=1).grid(row=7, column=0)
ttk.Radiobutton(root, text="decrypt", variable=var, value=2).grid(row=7, column=1)
buButton = ttk.Button(root, text="GO")
buButton.grid(row=9, column=3)
ttk.Label(root, text="key").grid(row=1, column=0, pady=10, padx=10)
Name = ttk.Entry(root, width=50)
Name.grid(row=1, column=1, columnspan=2, pady=10)
try:
	buButton.config(command=lambda: onc(filename))
except:
	messagebox.showerror(title="Opss", message="plese select your choices ")
buButton1 = ttk.Button(root, text="browse")
buButton1.grid(row=9, column=0)
buButton1.config(command=filename)


root.mainloop()
