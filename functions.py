'''def function_1():
    print("This is inside the function and the fucntion has been called")
print("this is outide the fuction")
function_1()
'''

'''def function_2(x):
    return 2*x
a=function_2(3)

print(a)'''

'''def function_3(x, y):
    return x+y
e=function_3(3, 4)
print(e)'''

'''BMI CALCULATOR USING FUCNTIONS'''

name1="Josh"
weight1_kg=24
height1_m=1.2

name2="Amy"
weight2_kg=500
height2_m=1.2


def bmi_calculato(name, weight_kg, height_m):
    bmi= weight_kg/(height_m**2)
    if bmi>2:
        print(name+"You are overweight")
    else :
        print(name+"You are not overwirhgt")

a=bmi_calculato(name1, weight1_kg, height1_m)
print(a)