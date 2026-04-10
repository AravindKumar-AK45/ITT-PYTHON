
 email = input("Enter your Gmail address: ").strip().lower()


if "@gmail.com" in email:
    user_part = email.split("@")[0]
    
    
    
    if user_part and " " not in email and email.endswith("@gmail.com"):
        print("Valid Gmail address!")
    else:
        print("Invalid format.")
else:
    print("Not a Gmail address.")







