from atm1 import atmoperations
from atm3 import DepositeError,WithdrawError,InsufError
bal=500.00
def deposite():
    global bal
    damt=float(input("enter the  deposited balence:"))
    if damt<0:
        raise DepositeError
    else:
        global bal
        bal+=damt
        print("ur account XXXXXXX123 created with INR:{}".format(damt))
        print("now ur account XXXXX123 after deposite INR:{}".format(bal))
def Withdraw():
    global bal
    wamt=float(input("enter the  deposited balence:"))
    if bal<=wamt:
        raise WithdrawError
    elif (wamt+500)>bal:
        raise InsufError
    else:
        bal-=wamt
        print("ur account XXXXXXX123 withdraw with INR:{}".format(wamt))
        print("now ur account XXXXX123 after deposite INR:{}".format(bal))
def Balenq():
    print("now ur account XXXXX123 after deposite INR:{}".format(bal))


