# starting the conversion of python into c
# including header files and main
def start_c():
    return "#include<stdio.h>\nint main(){"
# ending C program and 
def end_c():
    return "return 0;\n}"
# for print statement 
def print_statement(string):
    return f'printf("{string}");'

# dealing with if 
def open_if(condition):
    res="if (" + condition + ")\n{"
    return res

# dealing with if 
def close_if():
    return "}"



if __name__ == "__main__":
    pass
