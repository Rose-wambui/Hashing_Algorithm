import hashlib
import tkinter 


# working on the GUI part of the hashing algorithm

window = tkinter.Tk()
window.title("The Hashing algorithm by Rose")
window.geometry("600x400")
#window.config(bg="black")

hash_entry = tkinter.Entry(window, width=80)
hash_entry.pack()


# working on the functioning part
def hashed():
    password = hash_entry.get() 
    md_5 = hashlib.md5()  
    md_5.update(password.encode()) 
    hashed_md5 = md_5.hexdigest()  
    entry1.insert(0, hashed_md5)  

    sha_256 = hashlib.sha256()  
    sha_256.update(password.encode()) 
    hashed_sha256 = sha_256.hexdigest()  
    entry2.insert(0, hashed_sha256)

    sha_512 = hashlib.sha512()  
    sha_512.update(password.encode()) 
    hashed_sha512 = sha_512.hexdigest()  
    entry3.insert(0, hashed_sha512)
    
    



# i want to create a new frame where i will put all the hashes label

hash_frame = tkinter.Frame(window, padx=20, pady=20)
hash_frame.pack()

#createing the labels and entries for the hashes
label1 = tkinter.Label(hash_frame, text="MD5", padx=10, pady=10)
label1.grid(row=0, column=0,sticky="news")

entry1 = tkinter.Entry(hash_frame, width=80)
entry1.grid(row=0, column=1, sticky="news")


label2 = tkinter.Label(hash_frame, text="SHA256",padx=10, pady=10)
label2.grid(row=1, column=0)

entry2 = tkinter.Entry(hash_frame)
entry2.grid(row=1, column=1,sticky="news")


label3 = tkinter.Label(hash_frame, text="SHA512",padx=10, pady=10)
label3.grid(row=2, column=0,)

entry3 = tkinter.Entry(hash_frame)
entry3.grid(row=2, column=1,sticky="news")

button = tkinter.Button(window, text="Generate" ,command=hashed)
button.pack()



window.mainloop()




