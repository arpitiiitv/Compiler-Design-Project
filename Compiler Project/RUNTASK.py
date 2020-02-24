from C_template import start_c,end_c,print_statement,open_if,close_if
from condition import if_open,if_close,inside_if
if __name__ == "__main__":
    print("Cross Compiler")
    take_user_inputt=input("Enter python code: ")
    print("\n\n")
    #open file to store output
    with open("output.c","w") as f:
            
        #printing start template of C
        print(start_c())
        f.write(start_c())
        # printing statement
        if(take_user_inputt[0:5]=='print'):
            data=take_user_inputt[7:-2]
            data=data+"\\n"
            print(print_statement(data))
            f.write(print_statement(data))
        
        # dealing with conditions
        '''if(take_user_inputt[0:2]=="if"):
            x=take_user_inputt.find(')')
            condition=take_user_inputt[3:x]
            print(open_if(condition))
            f.write(open_if(condition))
            print(close_if())
            f.write(close_if())
        '''
        if(take_user_inputt[0:2]=='if'):
            x=take_user_inputt.find(":")
            stmt=take_user_inputt[2:x]
            print(if_open(stmt))
            f.write(if_open(stmt))
            if(take_user_inputt[1+x]=='\n'):
                print("YES")
        # dealing with loops

        # dealing with maths 

        #printing start template of C
        print(end_c())
        f.write(end_c())