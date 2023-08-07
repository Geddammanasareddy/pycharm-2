#ATM MAIN PROGRAM
from atm1 import atmoperations
from atm4 import deposite,Withdraw,Balenq
from atm3 import *
while(True):
    try:
        atmoperations()
        ch=int(input("enter our choice:"))
        match(ch):
            case 1:
                try:
                    deposite()
                except DepositeError:
                    print("dont try to -ve value and zero and values")
                except ValueError:
                    print("dont try to deposite alnum,space and symbols")

            case 2:
                try:
                    Withdraw()
                except WithdrawError:
                    print("dont try to -ve value and zero and values")
                except InsufError:
                    print("u dont have stuff funds--read python notes")
                except ValueError:
                    print("dont try to deposite alnum,space and symbols")
            case 3:
                Balenq()
            case 4:
                print("TNX for our program")
            case _:
                print("ur selection process is wrong-try again")
    except ValueError:
        print("Dont enter alnums,str,symbols for choice of ATM Operations")