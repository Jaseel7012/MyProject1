#create contact book
import phonenumbers


Names=[]
phoneNum=[]
n=int(input("enter number of items add..."))
for i in range(n):
    Name=input("Name..")
    phone_num=input("Phone Number:")
    Names.append(Name)
    phoneNum.append(phone_num)
print("\n Name \t\t\t Phone Numbers")
for i in range(n):
    print("{}\t\t\t{}".format(Names[i],phoneNum[i]))
#search 
search_item=input("enter name")
if search_item in Names:
    ind=Names.index(search_item)
    phone_num=phoneNum[ind]
    print("Name..{}: {}".format(search_item,phone_num))
else:
    print("name not found")
