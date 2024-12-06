username=input("enter:")
def validate_username(x):
    if x.isalnum() and 6<=len(x)<=15:
        print("validate username!")
    else:
        print("invalid username.only alphabets and numbers,6-15 characaters long. ")    
    validate_username(username)    