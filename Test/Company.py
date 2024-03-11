
l=11

def sub():
    a=10
    b=20
    c=a-b
    print(c)



# ----------------import module-------------------

import  Employee
# var
print(Employee.a)

# fun
Employee.add()

# --------------import module as new ---------------
import  Employee as e

# var
print(e.a)

# fun
e.add()

# ------------import module 1,module 2---------------------


import  Employee,Client

# var
print(Employee.a)
print(Client.l)

# fun
Employee.add()
Client.div()


# ------------import moudle1 as new,moudle2 as new---------
import Employee as e,Client as c


print(e.a)
print(c.l)

e.add()
c.div()



# ------------from moudle import var---------------
from Employee import a

print(a)

# -----------from module import fun------------
from  Employee import add

add()

# -----------from module imprt var as new var------------
from  Employee import a as p

# -----------from module imprt fun as new var----------
from Employee import add as cal

# ----------from moudle imort *----------------------
from  Employee import *














