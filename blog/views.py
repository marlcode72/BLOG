from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateForm

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwars):
        context={

        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)


    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = PostCreateForm(request.POST)
            if request
        context={
        }
        return render(request, 'blog_create.html', context)