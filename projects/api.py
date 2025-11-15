from .schema import CategorySchema , ProjectSchema , NotFoundSchema
from .models import Category , Project
from django.contrib.auth.decorators import login_required
from ninja import NinjaAPI , Schema
from django.shortcuts import get_object_or_404

api = NinjaAPI()



@api.post("/projects", response={201: ProjectSchema})
def create_project(request, project: ProjectSchema):
    project = Project.objects.create(**project.dict())
    return project

@api.get("/projects/{project_id}", response={200: ProjectSchema, 404: NotFoundSchema})
def project(request, project_id: int):
    try:
        project = Project.objects.get(pk=project_id)
        return 200, project
    
    except Project.DoesNotExist as e:
        return 404, {"message": "Project ID does not exist"}
    

@api.post("/categories", response={201: CategorySchema})
def create_category(request, category: CategorySchema):
    category = Category.objects.create(**category.dict())
    return category

