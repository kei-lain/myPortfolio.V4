from ninja import Schema, ModelSchema
from .models import Category, Project



class CategorySchema(Schema):
    category_name: str

    def _str_(self):
        self.category_name

class ProjectSchema(Schema):
    name: str
    programmingLanguages: str
    framework: str
    description: str
    category: str
    url: str
    demonstrationVideo: str
    project_id: int

    def _self_(self):
        self.name


class NotFoundSchema(Schema):
    message: str