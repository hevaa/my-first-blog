from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Item
from .forms import PostForm

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def cv_page(request):
    items = Item.objects.all()
    return render(request, 'blog/cv_display.html', {'items': items})

def cv_edit(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/cv/edit')

    items = Item.objects.all()
    return render(request, 'blog/cv_edit.html', {'items': items})

def cv_add(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], category=request.POST['item_category'] )
        return redirect('/cv/edit/add')

    items = Item.objects.all()
    return render(request, 'blog/cv_add.html', {'items': items})

def cv_delete(request):
    if request.method == 'POST':
        Item.objects.filter(id=request.POST['item_ID']).delete()
        return redirect('/cv/edit/delete')

    items = Item.objects.all()
    return render(request, 'blog/cv_delete.html', {'items': items})