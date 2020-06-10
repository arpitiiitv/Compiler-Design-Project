from statement import inside
def for_loop(data):
    temp=data.split(" ")[-1]
    n=inside(temp)
    i=str(data[1])
    return "for ( int "+str(i)+'=0;'+str(i)+"<"+ n +";"+str(i)+"++){"


def while_loop(data):
    return "while ("+data+ "){"
