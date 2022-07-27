import re

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

x = int(input('enter 1 or 2:'))
if x ==1:
        email=input("Enter your email:")
        b=0
        c=0
        d=0
        if len(email)>=6:  #1
            if email[0].isalpha():  #2
                if ("@" in email) and (email.count("@")==1):  #3
                    if (email[-3]==".") ^ (email[-4]=="."):  #4
                        for a in email:
                            if a==a.isspace():
                                b=1
                            elif a.isalpha():
                                if a==a.upper():
                                    c=1
                            elif a.isdigit():
                                continue
                            elif a=="_" or a=="." or a=="@":
                                continue
                            else:
                                d=1


                        if b==1 or c==1 or d==1:  #5
                            print("incorrect email 5")
                        else:
                            print("you entered correct email")
                    else:
                        print("incorrect email 4")
                else:
                    print("incorrect email  3")
            else:
                print("Wrong email 2")
        else:
            print("Incorrect email 1")
elif x==2:
    email = input('enter email:')
    isValid(email)
else:
    print("Invalid Input. Try again!")

