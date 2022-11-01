from pydantic import BaseModel, Field


class PaginationModel(BaseModel):
    query: str = Field(default="")
    page: int = Field(default=1)
    pre_page: int = Field(default=10)


class UserModel(BaseModel):
    username: str = Field(default="")
    nickname: str = Field(default="")
    password: str = Field(default="")
    mobile: str = Field(default="")
    email: str = Field(default="")
    gender: str = Field(default="")
    education: str = Field(default="")
    state: bool = Field(default=False)


class DepartmentModel(BaseModel):
    address: str = Field(default="")
    name: str = Field(default="")
    email: str = Field(default="")
    leader: str = Field(default="")
    pid: str = Field(default="")
    phone: str = Field(default="")
    sort: str = Field(default="")
    enable: str = Field(default="")


class RoleModel(BaseModel):
    name: str = Field(default="")
    desc: str = Field(default="")


class PermissionModel(BaseModel):
    pid: int = Field(default=0)
    name: str = Field(default="")
    code: str = Field(default="")
    level: str = Field(default="")
    path: str = Field(default="")
    open_type: str = Field(default="")
    icon: str = Field(default="")
    sort: int = Field(default="")

