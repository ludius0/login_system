# login_system

MODULES: tkinter, sqlite3, cryptography.fernet

My attempt to make a program with encrypted database and GUI. Tkinter and SQLite3 are preinstalled with python (you've to only pip install cryptography)

The program has three buttons: login, register, Generate new\n database and key. Your inputs are encoded and than compared with decrypted database.

If there is match in register your request is declined. If there is match with signing in than you're request is accepted. 

The third option (Generate... button) will delete content of database and create new cryptography key (for encryption and decryption).
