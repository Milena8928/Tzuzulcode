from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Post, Comment
# Create your views here.

def home(request):
    return render (request, 'home.html')

def posts(request):
    posts = Post.objects.all().order_by("created_date", "-id") #equivalente a SELECT * FROM posts ordenado de los mas recientes al mas antiguo .order_by("created_date")

    print(posts)
    #return HttpResponse("Publicaciones")
    return render(request, 'posts/posts.html', {
        'posts': posts
    })

def post(request, id):
    post= Post.objects.get(id=id)
    
    return render(request, 'posts/post.html',{
        'post': post
    })

def create_post(request):
    if request.method == "POST":
        post = Post(
            title=request.POST['title'],
            description=request.POST['description'],
            img=request.POST['image'],
            content=request.POST['content'],
            
        )

        post.save()

        return redirect("/posts")

    return render(request, 'posts/create.html')


def edit_post(request, id):
    post= Post.objects.get(id=id)
    if request.method == "POST":
        
            post.title=request.POST['title']
            post.description=request.POST['description']
            post.img=request.POST['image']
            post.content=request.POST['content']

            post.save()
            return redirect("/posts")
    return render(request, 'posts/edit.html', {'post': post})
         
def delete_post(request, id):
    post= Post.objects.get(id=id)
    post.delete()
    return redirect("/posts") 

def comment_post(request, id):
    post= Post.objects.get(id=id)
    if request.method == 'POST':
        comment = request.POST['comment']
        if comment:
            #save the values
            new_comment = Comment.objects.create(
                body = comment,
                activate = True,
            )
            
            new_comment.post = post
            new_comment.save()
            return redirect("/posts")

    return render(request, 'posts/comment.html',{
        'comment':comment,
        'new_comment':new_comment,
    })