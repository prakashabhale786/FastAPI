class rectangle:    # we make a class which name is rectangle
    def __init__(self,w:int,h:int) -> None:    # here we gave bydefoult function(init) when we use class there we need init()
        #becouse the init function is return class object like rectangle
        self.width=w   # here we store the values
        self.height=h


def area(r:rectangle)->int:   # we use  area function here  and rectangle means what ever there in rectangle we return here 
               # and output int   # we change here rectangle name to rectangle to r
    return r.width*r.height    #r mean rectangle



r1=rectangle(10,20)    # here we throw and store the value of the w and h
print("area=", area(r1))


 # here we done type casting
# output is 200