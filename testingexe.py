import tkinter as tk

def on_click():
    label.config(text = "Hello, Windows 11!")

app = tk.Tk()
app.title("My first app")
app.geometry("300x200")

label = tk.Label(app, text="Click the button")
label.pack(pady = 20)

button = tk.Button(app, text = "Click Me", command = on_click)
button.pack()

app.mainloop()