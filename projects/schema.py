from ninja import Schema, ModelSchema
from .models import Category, Project , Framework , ProgrammingLanguage, Blog



class CategorySchema(Schema):
    category_name: str

    def _str_(self):
        self.category_name




class ProjectSchema(ModelSchema):
    class Meta:
        model = Project
        fields = '__all__'
    

class BlogSchema(ModelSchema):
    class Meta:
        model = Blog
        fields = '__all__'

class NotFoundSchema(Schema):
    message: str


