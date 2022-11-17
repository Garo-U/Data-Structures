user_pin = int(input("Enter Pin : "))
user_name = input("Enter Name : ")
user_balance = int(input("Enter Balance : "))
user = {
    'pin': user_pin,
    'balance': user_balance,
    'name': user_name
}

def widthdraw_cash():
    while True:
        amount_w = int(input("Enter the amount of money you want to widthdraw: "))
        if amount_w > user['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount_w
            print(f"Cash Withdrawl Success ! {user['balance']}")
            return False

def balance_enquiry():
    print(f"Total balance {user['balance']} Dollars")
    

def deposit_cash():
    while True:
        amount_d = int(input("Enter the amount of money you want to Deposit : "))
        user['balance'] +=  amount_d
        print(f"Cash Deposit Success ! {user['balance']}")
        return False




while True:

    print("Welcome to Bank of Swiss")

    pin = int(input('Please enter your four digit pin: '))

    if pin == user['pin']:
        
        print("what do you want to do")
        print(" Enter 1 to Widthdraw Cash \n Enter 2 for Balance Enquiry \n Enter 3 to Deposit cash\n")

        query = int(input("Enter Task: "))

        if query == 1:
            widthdraw_cash()
        elif query == 2:
            balance_enquiry()
        elif query == 3:
            deposit_cash()
        
        else:
            print("Please enter a correct value shown")
    else:
        print("Entered wrong pin")
    
    x = input("Run Again Transaction (Y/N) : ").lower()
    if (x == "n"):
        break
