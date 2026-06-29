import hashlib

print("=== Secure Login System ===")

username = input("Create Username: ")
password = input("Create Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\nRegistration Successful!")

print("\n=== Login ===")

login_user = input("Username: ")
login_pass = input("Password: ")

login_hash = hashlib.sha256(login_pass.encode()).hexdigest()

if login_user == username and login_hash == hashed_password:
    print("\n✅ Login Successful")
else:
    print("\n❌ Invalid Username or Password")