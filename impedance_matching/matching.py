from l_match import lml,lmh
from t_match import tml,tmh
from pi_match import pml,pmh
def main():
    print("Choose any one of the Following filter type")
    print("1.LPF")
    print("2.HPF")
    op=int(input("Enter Your option:"))

    if(op==1):
        print("Choose one of the topology")
        print("1.L_Matching Network")
        print("2.Pi_matching Network")
        print("3.T_matching Network")
        choice=int(input("Enter Your option:"))
        if(choice==1):
            lml() #Low pass L match
        elif(choice==2):
            pml() #Low pass pi match
        elif(choice==3):
            tml() #Low pass T match
        else:
            exit()
    elif(op==2):
        print("Choose one of the topology")
        print("1.L_Matching Network")
        print("2.Pi_matching Network")
        print("3.T_matching Network")
        print("Choose one of the topology")
        print("1.L_Matching Network")
        print("2.Pi_matching Network")
        print("3.T_matching Network")
        choice=int(input("Enter Your option:"))
        if(choice==1):
            lmh() #HIgh pass L match
        elif(choice==2):
            pmh() #HIgh pass pi match
        elif(choice==3):
            tmh() #HIgh pass T match
        else:
            exit()
    else:        
        exit()


if __name__=="__main__":
    main()