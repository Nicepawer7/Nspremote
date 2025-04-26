import tkinter as tk
 
window = tk.Tk()
greeting = tk.Label(text="hello everyone \n what's up")
greeting.pack()
 
entry = tk.Entry(window)
entry.pack()
 
text_box = tk.Label()
text_box.pack()
 
 
def on_entry(event):
    text_box['text'] = name = entry.get()
    print(name)
 
 
entry.bind('<Return>', on_entry)
 
window.mainloop()