def if_open(stmt):
    return f"if ({stmt}) "+'\n{'

def inside_if(stmt):
    return "iside if"


def if_close():
    return '}'

if __name__ == "__main__":

    print(if_open('x>y'))
    print(if_close())