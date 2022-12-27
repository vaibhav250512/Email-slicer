def main():
    print("Welcome to the E-mail slicer : ")
    print("")
    
    email_input = input("Input your Email")
    
    (username, domain) = email_input.split("@")
    (domain, extention) = domain.split(".")
    
    print("username : ", username)
    print("Domain : ", domain)
    print("Extention : ", extention)
    
main()