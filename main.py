try:
    import faker
    from faker import providers
    from faker import Faker
    import tkinter as tk
    from tkinter import messagebox
    from PIL import Image, ImageTk
    from config import config
    import os
except Exception as e:
    print(e)

fake = Faker()
app = tk.Tk()
app.title("Card Generator")

# Entries



# Button Function----


cards = []
def button_function():
    try:
        amount = int(entry.get())
    except:
        messagebox.showinfo("Popup", "Please provide a number!")
    

    
    for _ in range(amount):
        generated_text = f"{fake.credit_card_full(card_type=config.card_provider)}\n-------------------------------\n"
        generated = text_widget.insert("1.0", generated_text)
        cards.append(generated_text)
    
    scrollbar = tk.Scrollbar(app, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)
        
        
        
    def saveButton_function():    
        filename = f"generated_cards.txt"
        with open(filename, "w") as file:
            file.writelines(cards)
        messagebox.showinfo("Popup", f"Saved card details to {filename}")
        saveButton.config(text="Saved")
    
    
    label.pack_forget()
    entry.pack_forget()
    button.pack_forget()
    
        
            
            
    saveButton = tk.Button(text="Save to Text file", command=saveButton_function)
    saveButton.pack(anchor="nw")




logo = Image.open("files\images\logo.png")
width, hight = 90, 90
logo = logo.resize((width, hight))
logoimage = ImageTk.PhotoImage(logo)

logolabel = tk.Label(app, image=logoimage)
logolabel.pack()

configlabel = tk.Label(app, text="You can change the card provider from the config file!", padx=5, pady=5)
configlabel.pack()
label = tk.Label(app, text="how many Cards do you want to generate?", padx=5, pady=5)
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Generate", command=button_function)
button.pack()

text_widget = tk.Text(app, wrap="word", font=("Arial", 12))
text_widget.pack(expand=True, fill="both")

    
app.iconbitmap("files\images\logo.ico")
app.mainloop()
