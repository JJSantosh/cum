dict1={'welcome':10,'to':2,'my':10,'code':10}
print("Dictionary:"+ str(dict1))
x=int(input("Enter the number to check frequency:"))
res=0
for key in dict1:
    if dict1[key] == x:
        res=res+1

print("Frequency of x:"+str(res))