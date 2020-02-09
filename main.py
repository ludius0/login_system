from tkinter import *
from tkinter import messagebox
#from cryptography.fernet import Fernet
from getpass import getpass
import sqlite3
import os

# Set up main screen
root = Tk()
root.title("Login")
root.geometry("500x500")

# Set up cryptography
#f = Fernet(key)

# Connect database
conn = sqlite3.connect('login_database.db')
c = conn.cursor()


#Set up non existing database
if not os.walk("login_database.db"):
    c.execute('''CREATE TABLE user_data (
                    username text,
                    password text,
                    first_name text,
                    last_name text
                    )''')

### Functions ###
#Generate new key and database
def generate_key_and_db():
    pass

# Pop up window with login inputs
def login():
    # Set up sign in screen
    root1 = Tk()
    root1.title("Sign in")
    root1.geometry("300x400")

    # Connect database
    conn = sqlite3.connect('login_database.db')
    c = conn.cursor()   


    try:
        pass
    except Exception as E:
        pass

    # Close connection to database
    conn.commit()
    conn.close()


    root1.mainloop()

# Register to database
def sign_up_to_db():
    # Connect database
    conn = sqlite3.connect("login_database.db")
    c = conn.cursor()

    username = r_username_entry.get()
    password = r_password_entry.get()
    first_name = r_first_name_entry.get()
    last_name = r_last_name_entry.get()
    

    # Execute in database
    c.execute("INSERT INTO user_data VALUES (:username, :password, :first_name, :last_name)",
                        {
                            "username": username,
                            "password": password,
                            "first_name": first_name,
                            "last_name": last_name
                        })

    # Close connection to database
    conn.commit()
    conn.close()
    

# Pop up window with register inputs
def register():
    global r_username_entry, r_password_entry, r_first_name_entry, r_last_name_entry
    #Set up register screen
    root2 = Tk()
    root2.title("Sign in")
    root2.geometry("300x400")


    ### Labels, Entry and Button
    r_username_label = Label(root2, text="Username:").grid(row=0, column=0)
    r_password_label = Label(root2, text="Password:").grid(row=1, column=0)
    r_first_name_label = Label(root2, text="First name:").grid(row=2, column=0)
    r_last_name_label = Label(root2, text="Last name:").grid(row=3, column=0)
    
    r_username_entry = Entry(root2)
    r_username_entry.grid(row=0, column=1)
    r_password_entry = Entry(root2)
    r_password_entry.grid(row=1, column=1)
    r_first_name_entry = Entry(root2)
    r_first_name_entry.grid(row=2, column=1)
    r_last_name_entry = Entry(root2)
    r_last_name_entry.grid(row=3, column=1)

    sign_up = Button(root2, text="Register to database", command=sign_up_to_db).grid(row=4, column=1)
    ###

    # Loop
    root2.mainloop()

### Functions ###





# Labels
username_label = Label(root, text="Username:").grid(row=0, column=0)
password_label = Label(root, text="Password:").grid(row=1, column=0)

# Entry
username_entry = Entry(root)
username_entry.grid(row=0, column=1)
password_entry = Entry(root)
password_entry.grid(row=1, column=1)

# Buttons
sign_in_b = Button(root, text="Sign In", command=login).grid(row=2, column=1)
register_in = Button(root, text="Register", command=register).grid(row=3, column=1)
restart = Button(root, text="Generate new\n database and key", command=generate_key_and_db).grid(row=4, column=1)

# Close connection to database
conn.commit()
conn.close()

# Loop
root.mainloop()
