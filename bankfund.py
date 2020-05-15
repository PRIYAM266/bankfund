
a = input("Choose either admin or user: ")

Admin1 = ["Welcome Raj, your Bank Account Number = 564349067 contains Funds Rs. 3,12,000"]
Admin2 = ["Welcome Ram, your Bank Account Number = 456723890 contains Funds Rs. 1,42,000"]


#Admin1 Password is 1234
#Admin2 Password is 2345

while True:
    if(a == "admin"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if(password == "1234"):
            print("\nAdmin1\n")
    
        elif(password == "2345"): 
            print("\nAdmin2\n")
        else:
    	    print("\nWrong Password\n")
    	    exit()
        print("Enter the account and name of the user you want to transfer funds to: ")
        name=input("Account holder name: ")
        ifsc = input("Enter the IFSC Code: ")
        account = int(input("Enter the Account Number: "))
        funds = int(input("Enter the amount of funds you want to transfer in Rs.: "))
        print("Your Entered details are as follows: ")
        print("Account holder name: "+ name)
        print("IFSC code: " +ifsc)
        print("Account Number: " +str(account))
        print("Fund: " +str(funds))    
        print("For Final Fund Transfer enter the OTP sent to your registered mobile number: ")
        otp=int(input())
        print("final balance :")
        if (password=="1234"):
            print(312000-funds)
        else:
            print(142000-funds)
        exit()
    else: 
        print("You are not authorised to use this function!!!")
        exit()