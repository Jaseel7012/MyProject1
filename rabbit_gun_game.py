import random
print("""Winning Rules of Rabbit gun Wall game :\n rabbit vs gun -> gun wins\n
 rabbit vs wall ->rabbit wins \n wall vs gun -> wall wins \n""")
while True:
    print("Enter choice  \n 1 for rabbit \n 2 for gun \n 3 for wall \n")
    user_trn=int(input("User Turn.."))
    while user_trn >3 or user_trn<1:
        user_trn=int(input("enter valid input between 1 and 3"))
    if user_trn==1:
        choice_item="rabbit"
    elif user_trn==2:
        choice_item="gun"
    elif user_trn==3:
      choice_item="wall"
    print("your choice is",choice_item)
    comp_trn=random.randint(1,3)
    if comp_trn==1:
        choice_item_cmp="rabbit"
    elif comp_trn==2:
        choice_item_cmp="rock"
    else:
        choice_item_cmp="wall"
    print("computer choice is..",choice_item_cmp)
   
    if (user_trn==1 and comp_trn==2) or (user_trn==2 and comp_trn==1):
        print("gun wins \n")
        res="gun"
    elif (user_trn==1 and comp_trn==3) or (user_trn==3 and comp_trn==1):
        print("rabbit wins")
        res="rabbit"
    elif (user_trn==2 and comp_trn==3) or (user_trn==3 and comp_trn==2):
        
        res="wall"
    else:
        res="draw"
        print("draw")
    if res==choice_item:
        print("***User wins***")
    elif res==choice_item_cmp:
        print("***Computer Wins***")
    else:
        print("Draw")
    print("Do you want to play again? (Y/N)")
    ans=input()
    if ans=='n' or ans=='N':
        break
