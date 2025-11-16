from .schema import CategorySchema , ProjectSchema , NotFoundSchema, BlogSchema
from .models import Category , Project, Blog
from django.contrib.auth.decorators import login_required
from ninja import NinjaAPI , Schema
from django.shortcuts import get_object_or_404

api = NinjaAPI()



@api.post("/projects", response={201: ProjectSchema})
def create_project(request, project: ProjectSchema):
    project = Project.objects.create(**project.dict())
    return 201, project



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

@api.post("/blog", response={201: BlogSchema})
def create_blog_post(request, blog: BlogSchema):
    blog = Blog.objects.create(**blog.dict())
    return 201, blog

@api.get("/blog/{blog_id}", response={200: BlogSchema, 404: NotFoundSchema})
def get_blog(request, blog_id: int):
    try:
        blog = Blog.objects.get(pk=blog_id)
        return 200, blog
    
    except Blog.DoesNotExist as e:
        return 404, {"message:": "Blog post doesn't exist"}
    





