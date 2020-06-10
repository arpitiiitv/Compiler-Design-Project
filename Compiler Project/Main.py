from collections import defaultdict
from statement import  print_stmt,inside
from CPP_template import start,end
from condition import if_condition,close,elif_condition
from loop import for_loop,while_loop

#Take input file name by the user without .py extension
input1 = input("enter python file : ")

#open input file in read mode
inp = open(input1+".py","r")

#initilize a output file in advance write mode
#name output file as OUTPUTfilename.cpp
out = open("OUTPUT"+input1+".cpp","w+")

#read data from input file stream
data = inp.read()
#it will print python code on console
print(data.split("\n"))
#store all the information in Stack
data = data.split(("\n"))

#type of data we are dealing with
print(type(data))
#variables to store how many if,else,for,while was in the python code
if_count = 0
else_count = 0
elif_count = 0
while_count=0
for_count = 0

#how many variable are there and its type 
#stoe the details in HashMap
variables=defaultdict(list)

#print the start of the c++ template
print(start())
#store the start of the c++ template in output
out.write(start())
# make sure there is newline after each line
out.write("\n")

#Getting all the information of loops,conditions
for line in data:
    if "if " in line:
        if_count+=1
    elif "elif " in line:
        elif_count+=1
    elif "else " in line:
        else_count+=1
    elif "for " in line:
        for_count+=1
    elif "while " in line:
        while_count+=1

#processing the data line by line
for line in data:
    # printing statement
    if (line[0:5]=="print") :
        print(print_stmt(inside(line[5:])))
        out.write(print_stmt(inside(line[5:])))
        out.write("\n")
         
    elif (line[0:9]=="    print"):
        print(print_stmt(inside(line[9:])))
        out.write(print_stmt(inside(line[9:])))
        out.write("\n")


    # conditions handling
    elif line[0:2]=="if":
        print(if_condition(line[2:len(line)-1]))
        out.write(if_condition(line[2:len(line)-1]))
        if_count-=1
        out.write("\n")

    #if after for loop or while loop
    elif line[4:6]=="if":
        print(if_condition(line[4:len(line)-1]))
        out.write(if_condition(line[2:len(line)-1]))
        if_count-=1
        out.write("\n")
    elif line[0:4]=='elif':
        print(elif_condition(line[4:len(line)-1]))
        out.write(elif_condition(line[4:len(line)-1]))
        out.write('\n')
        print(close())
        out.write(close())
        out.write("\n")
    
    # loop handling
    elif line[0:3]=="for":
        for_count-=1
        print(for_loop(line[3:len(line)-1]))
        out.write(for_loop(line[3:len(line)-1]))
        out.write("\n")
    elif line[0:5]=="while":
        while_count+=1
        print(while_loop(line[5:len(line)-1]))
        out.write(while_loop(line[5:len(line)-1]))
        out.write('\n')
        
        ####################
    temp=line.split(" ")
    
    if "max" in temp:
        if temp[2]=="max":
            print("int "+"".join(temp)+';')
            out.write("int "+"".join(temp))
            out.write('\n')
    if "min" in temp:
        if temp[2]=="min":
            print("int "+"".join(temp)+';')
            out.write("int "+"".join(temp))
            out.write('\n')
    if "abs" in temp:
        if temp[2]=="abs":
            print("int "+"".join(temp)+';')
            out.write("int "+"".join(temp))
            out.write('\n')
        
        


    # Airthmatic operations

print(close())
out.write(close())
        
#print the end of the c++ template
print(end())
#store the end of the c++ template in output file
out.write(end())
out.write("\n")
inp.close()
out.close()