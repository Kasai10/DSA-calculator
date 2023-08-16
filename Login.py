import customtkinter as tk
import CreateCharacter
import Database

def show_password():
    if checkBox.get() == 1:
        password_entry.configure(show = "")
    else:
        password_entry.configure(show = "*")


tk.set_default_color_theme("green")
tk.set_appearance_mode("dark")

window = tk.CTk()

window.geometry("600x200")
window.title('Login')

frame = tk.CTkFrame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

label = tk.CTkLabel(frame, text='Willkommen, bitte logge dich ein!', font=('Arial', 30))
label.grid(pady = 20, row = 0,  sticky = "NSEW", columnspan = 100, padx = 60)

name_entry = tk.CTkEntry(frame, font=('Arial', 16), placeholder_text='Name')
name_entry.grid(row = 1, column = 0, sticky = "NSEW", padx = 150, columnspan = 100)

password_entry = tk.CTkEntry(frame, font=('Arial', 16), placeholder_text='Passwort', show = "*")
password_entry.grid(pady = 20, row =2, column = 0, sticky = "NSEW", columnspan = 100, padx = 150)

checkBox = tk.CTkCheckBox(frame, command = show_password, text= "")
checkBox.grid(row = 2, column = 4, sticky = "NSEW")




def character():
    window.withdraw()
    CreateCharacter.show_character_creation()

def login():
    window.withdraw()
    Database.databaseLogic("login", name_entry= name_entry.get(), password_entry= password_entry.get())


login = tk.CTkButton(frame, text= 'Login', font=('Arial', 16), command=login)
login.grid(row=5, column=0, padx = 100)

create = tk.CTkButton(frame, text= 'Charakter erstellen', font=('Arial', 16), command=character)
create.grid(row=5, column=3, padx = 20)


frame.pack()
window.mainloop()


