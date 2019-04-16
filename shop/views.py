from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.decorators.http import require_POST
from .models import Category, Product, Post, Themes, Filt 
from cart.forms import CartAddProductForm
from .forms import PostForm
from django.conf import settings
from django.utils import timezone
from django.shortcuts  import redirect





def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
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

# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    }) 
 
def ThemeList(request,theme_slug=None):
    theme = None
    themes = Theme.objects.all()
    products = Product.objects.filter(available=True)
    if theme_slug:
        theme = get_object_or_404(Theme, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/index.html', {
        'theme': theme,
        'themes': themes,
        'products': products
    }) 
 
    return

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})
#Stranica glavnoi
def Index(request,category_slug=None):
    lastposts = []
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[0:2]
    themes = Themes.objects.all()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)      
    return render(request, 'shop/product/index.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'posts':posts,
        'themes':themes,
    }) 