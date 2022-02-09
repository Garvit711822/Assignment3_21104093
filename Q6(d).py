dict={}
first_sid=input("Enter sid of student:")
dict[first_sid]=input("Enter name of student:")
while True:
    add_more=input("Do you want to add more students?if yes write Y nor N:")
    if(add_more=='Y'):
        p=input("Enter sid of student:")
        dict[p]=(input("Enter name of student:"))
    elif(add_more=='N'):
        break;
    else:
        print("Error! Only print Y or N")
i=input("Enter sid of student:")
for sid in dict.keys():
    if sid==i:
        name=dict[sid]
        print("The name of student is:",name)
    else:
        print("There is no student with sid:",i)