
# types hints means that variable value anly intager,strings,float like this

def division(a:int,b:int):   # we select datatypesin int becosebwe want to devide  # a dtype btype is only int
    return a/b
print(division(14,2))


def division(a:int,b:int)->int:   #  we want int output so we use it write before collen  
    return a/b
print(division(14,2))




def division(a:int,b:int)->float:   #  we want float output so we use it write before collen
    return a/b
print(division(14,2))


def division(a:int,b:int)->str:   #  we want strings output so we use it write before collen
    return a/b
print(division(14,2))



# output is 7