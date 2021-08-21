#Take a string input and print the number of occurances of each character
a=input("Enter the string:\n")
str=list(a)
new=[]

for i in str:
    if i not in new:
        new.append(i)
        count=0
        for j in range(len(str)):
            if i==str[j]:
                count+=1
        print("{} is {}".format(i,count))