#this file is outside of modules folder so to acess mymodule python file code is as follows:

from modules import mymodule    #from folder "modules" import python file "mymodule" 

mymodule.greeting("saloni")     #from "mymodule" python file access "greeting" function 
                                #under that greeting function we pass argument("saloni")
    
from modules import mymodule as name  #from folder"modules" imports "mymodule" named python file as "name" abrupt 
                                        #name kept for ease of acess in this particular python file

name.greeting("technojam")        #under name(mymodule) acess "greeting" function and pass technojam as its argument