from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(): 
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

  nr_letter = random.randint(8,10)
  nr_number = random.randint(2,4)
  nr_characters = random.randint(2,4)

  password_list = []

  for _ in range(nr_letter):
    password_list += random.choice(letters)

  for _ in range(nr_number):
    password_list += random.choice(number)

  for _ in range(nr_characters):
    password_list += random.choice(characters)

  password = ""
  for _ in password_list:
    password += _

  password_entry.insert(0,password)
  pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  new_data = {
    website:{
      'email':email,
      'password':password,
      }
      }

  if len(website) ==0 or len(password) ==0:
    messagebox.showinfo(title='Oops',message='Please fill all fields')
  else:
    try:
      with open('data.json','r') as data_file:
        # json.dump(new_data,data_file,indent=4)
        data = json.load(data_file)
        
    except:
      with open('data.json','w') as data_file:
        json.dump(new_data,data_file,indent=4)
    else:
      data.update(new_data)
      with open('data.json','w') as data_file:
        json.dump(data,data_file,indent=4)
    finally:
      website_entry.delete(0,END)
      email_entry.delete(0,END)
      password_entry.delete(0,END)
    
    
def find_password():
  website = website_entry.get()
  try:
    with open('data.json') as data_file:
      data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(title="Error",message='No Data File Found')
  else:
      if website in data:
        email = data[website]['email']
        password = data[website]['password']
        messagebox.showinfo(website,f'Email: {email}\nPassword: {password}')
        
      else:
        
        messagebox.showinfo(website,f'No Data for {website} were found')

  

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#2c3e50")  # Dark Blue Background

# Logo
canvas = Canvas(height=200, width=200, bg="#2c3e50", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, pady=20)  # Centering logo

# Labels
label_font = ("Arial", 12, "bold")
label_fg = "#ecf0f1"  # Light Grey Text

website_label = Label(text="Website:", font=label_font, bg="#2c3e50", fg=label_fg)
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:", font=label_font, bg="#2c3e50", fg=label_fg)
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:", font=label_font, bg="#2c3e50", fg=label_fg)
password_label.grid(row=3, column=0, sticky="e")

# Entry Fields
entry_bg = "#ecf0f1"
entry_fg = "#2c3e50"
entry_border = 2

website_entry = Entry(width=21, bg=entry_bg, fg=entry_fg, bd=entry_border)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()
email_entry = Entry(width=35, bg=entry_bg, fg=entry_fg, bd=entry_border)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
password_entry = Entry(width=21, bg=entry_bg, fg=entry_fg, bd=entry_border)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
btn_bg = "#3498db"  # Bright Blue Buttons
btn_fg = "#ffffff"
btn_font = ("Arial", 10, "bold")

search_button = Button(text="Search", width=14, command=find_password, bg=btn_bg, fg=btn_fg, font=btn_font)
search_button.grid(row=1, column=2, padx=5)
generate_password_button = Button(text="Generate Password", command=generate_password, bg=btn_bg, fg=btn_fg, font=btn_font)
generate_password_button.grid(row=3, column=2, padx=5)
add_button = Button(text="Add", width=36, command=save, bg="#27ae60", fg=btn_fg, font=btn_font)  # Green Add Button
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()