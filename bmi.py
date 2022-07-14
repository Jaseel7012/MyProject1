# from tkinter import Place


# class Student:
#     __name=None
#     m1=0
#     m2=0
#     def _total(self):
#         return self.m1+self.m2
#     def avg(self):
#         print(self._total()/2)
# s=Student()
# s.name="student"
# s.m1=99
# s.m2=45
# s.avg()
# print(s._total())
# print(s.name)
# s1=Student()
# s1.m1=50
# print(s1.m1)
# s1._to
hei=float(input("Enter your height in cm"))
wei=float(input("Enter your weight in kg"))
height=hei/100
BMI=wei/height**2
print("your body mass index is..",BMI)
if BMI>0:
    if BMI<18.5:
        print("you are underweight")
    elif BMI<=25:
        print("you are healthy")
    elif BMI<=30:
        print("you are overweight")
    else:
        print("severely overweight")
else:
    print("enter valid details")