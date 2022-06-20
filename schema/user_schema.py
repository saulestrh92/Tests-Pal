from pydantic import BaseModel, EmailStr, constr

class DataUser(BaseModel):
  email: EmailStr
  password: constr(min_length=5, max_length=18)