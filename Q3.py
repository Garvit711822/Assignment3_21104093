#taking input from user as list
first_number=int(input("Enter first number:"))
second_number=int(input("Enter second number:"))
third_number=int(input("Enter third number:"))
list=[first_number,second_number,third_number]
#Creating list of tupples with first element of list as a number and second as its square
new_list=[(i,i**2)for i in list]
print(new_list)
# print(list)