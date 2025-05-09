import hashlib;
users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users_db:
        print("Error: User already exists.")
    else:
        hashed = hash_password(password)
        users_db[username] = hashed
        print("Created new user")

def login(username, password):
    hashed = hash_password(password)
    stored_password = users_db.get(username)
    if stored_password is None:
        print("Error: User does not exist.")
    elif stored_password == hashed:
        print("Login Successful")
    else:
        print("Error: Incorrect password")
register("john", "mypassword")  
login("john", "mypassword")    
