from ninja import Schema
from pydantic import model_validator

from django.contrib.auth.models import User


class UserResponse(Schema):
    id: int
    username: str
    password: str


class UserRequest(Schema):
    username: str
    password: str
    confirm_password: str
    
    @model_validator(mode='after')
    def validate_registration(self):
        if self.password != self.confirm_password:
            raise ValueError("Password and Confirm Password must be same")

        if self.username.lower() in self.password.lower():
            raise ValueError("Register is invalid")

        if User.objects.filter(username=self.username).exists():
            raise ValueError("Username is duplicate")

        return self

