Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
new_set=(Set1|Set2|Set3)-((Set1&Set2&Set3)|(Set1&Set2)|(Set1&Set3)|(Set3&Set2))
print(new_set)