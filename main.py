from tkinter import *
from tkinter import messagebox
#from cryptography.fernet import Fernet
import sqlite3

# Set up main screen
root = Tk()
root.title("Login")
root.geometry("250x200")

# Connect database
conn = sqlite3.connect("login_database.db")
c = conn.cursor()

# Create new table if there isn't any
try:
    c.execute("""CREATE TABLE data (username text, password text, first_name text, last_name text)""")
except:
    pass

    
### Functions ###
#Generate new key and database
def generate_key_and_db():
    pass

def succesful_login(first_name, last_name):
    # Set up sign in screen
    root1 = Tk()
    root1.title("Sign in")
    root1.geometry("150x150")

    # Display first name and last name of username
    show_label = Label(root1, text=f"Welcome in, {first_name} {last_name}.").pack()

    root1.mainloop()

# Pop up window with login inputs
def login(username_entry, password_entry):
    statement = False

    #Save username and password from Entry (for better readability)
    username = username_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect('login_database.db')
    c = conn.cursor()   

    # Loop through database, compare username and password from Entry and get access to login-in window (succesful_login())
    try:
        dataCopy = c.execute("SELECT * FROM data")
        compare = dataCopy.fetchall()
        for i in compare:
           if username == i[0] and password == i[1]:
                statement = True
                first_name = i[2]
                last_name = i[3]
    except:
        messagebox.showerror("Error", "Something went wrong...")

    succesful_login(first_name, last_name) if statement else messagebox.showerror("Error", "Wrong username or password.")

    conn.commit()
    conn.close()

# Register to database
def sign_up_to_db(r_username_entry, r_password_entry, r_first_name_entry, r_last_name_entry):
    statement = True
    
    conn = sqlite3.connect("login_database.db")
    c = conn.cursor()

    # Convey data (for better readability)
    username = r_username_entry.get()
    password = r_password_entry.get()
    first_name = r_first_name_entry.get()
    last_name = r_last_name_entry.get()

    # Loop through database, compare username and password from Entry and save it to database
    try:
        dataCopy = c.execute("SELECT * FROM data")
        compare = dataCopy.fetchall()
        for i in compare:
           if username == i[0] and password == i[1]:
                statement = False
    except Exception as e:
        messagebox.showerror("Error", "Something went wrong...")

    # Execute in database
    if statement:
        c.execute("INSERT INTO data VALUES (?, ?, ?, ?)", (username, password, first_name, last_name))
        messagebox.showinfo("Info", "You have been succesfully register.")
    else:
        messagebox.showerror("Error", "Somebody has alredy this username/password.")    


    conn.commit()
    conn.close()

    # Close window if user get registered
    root2.destroy() if statement else None
    

# Pop up window with register inputs
def register():
    global root2
    #Set up register screen
    root2 = Tk()
    root2.title("Sign in")
    root2.geometry("250x250")


    ### Labels, Entry and Button
    r_username_label = Label(root2, text="Username:").grid(row=0, column=0)
    r_password_label = Label(root2, text="Password:").grid(row=1, column=0)
    r_first_name_label = Label(root2, text="First name:").grid(row=2, column=0)
    r_last_name_label = Label(root2, text="Last name:").grid(row=3, column=0)
    
    r_username_entry = Entry(root2)
    r_username_entry.grid(row=0, column=1)
    r_password_entry = Entry(root2, show="*")
    r_password_entry.grid(row=1, column=1)
    r_first_name_entry = Entry(root2)
    r_first_name_entry.grid(row=2, column=1)
    r_last_name_entry = Entry(root2)
    r_last_name_entry.grid(row=3, column=1)

    sign_up = Button(root2, text="Register to database", command=lambda:sign_up_to_db(r_username_entry, r_password_entry, r_first_name_entry, r_last_name_entry)).grid(row=4, column=1, ipady=10)
    ###
    
    root2.mainloop()


### MAIN LABELS, ENTRY AND BUTTONS
# Labels
username_label = Label(root, text="Username:").grid(row=0, column=0)
password_label = Label(root, text="Password:").grid(row=1, column=0)

# Entry
username_entry = Entry(root)
username_entry.grid(row=0, column=1)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Buttons
sign_in_b = Button(root, text="Sign In", command=lambda:login(username_entry, password_entry)).grid(row=2, column=1, ipadx=29, ipady=10)
register_in = Button(root, text="Register", command=register).grid(row=3, column=1, ipadx=26, ipady=10)
restart = Button(root, text="Generate new\n database and key", command=generate_key_and_db).grid(row=4, column=1)


### CLOSE ALL
# Close connection to database
conn.commit()
conn.close()

# Loop
root.mainloop()
