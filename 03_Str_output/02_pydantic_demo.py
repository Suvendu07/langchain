# from pydantic import BaseModel

# class Student(BaseModel):
    
#     name: str
    
# new_student = {'name':'suvendu'}
# # new_student = {'name':20} # if we do this it show error

# student = Student(**new_student)

# print(student)
# # print(type(student))



""" In pydantic we can set default value """

# from pydantic import BaseModel

# class Student(BaseModel):
    
#     name: str = 'suvendu'
    
# new_student = {}
# # new_student = {'name':20} # if we do this it show error

# student = Student(**new_student)

# print(student.name)
# # print(type(student))



""" Optional fields"""

"""if you want to specify some
validation like if age > 3 show me but sometime's 
it may show may be age < 3"""


# from pydantic import BaseModel
# from typing import Optional

# class Students(BaseModel):
    
#     name: str = 'suvendu'
#     age : Optional[int] = None
    
    
# new_student = {}


# # if you want to pass the age
# # new_student = {'age':20}

# student = Students(**new_student)

# print(student)



""" In pydantic can handle inside typeconsertion

if the age is pass number but in str format. pydantic can handle intenally and understand it 
and return a number in age."""

# from pydantic import BaseModel
# from typing import Optional

# class Students(BaseModel):
    
#     name: str = 'suvendu'
#     age : Optional[int] = None
    
    
# new_student = {'age':'20'}




# student = Students(**new_student)

# print(student)






"""Builtin Validation"""

# from pydantic import BaseModel, EmailStr
# from typing import Optional

# class Students(BaseModel):
    
#     name: str = 'suvendu'
#     age : Optional[int] = None
#     email: EmailStr
    
# # new_student = {'email':'abc'} # it show error bcz it is not a correct email
# new_student = {'email':'suvendukhuntia1234@gmail.com'}




# student = Students(**new_student)

# print(student)







"""Field function"""


from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Students(BaseModel):
    
    name: str = 'suvendu'
    age : Optional[int] = None
    email: EmailStr
    cgpa : float = Field(gt = 0 , lt = 10, default = 5, description = 'A decimal value representing cgpa of student')
    
# new_student = {'email':'abc'} # it show error bcz it is not a correct email
new_student = {'email':'suvendukhuntia1234@gmail.com', 'cgpa':8.9}




student = Students(**new_student)

print(student)