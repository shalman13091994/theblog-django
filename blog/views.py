from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy

# def home(request):
#   return render( request,'homepage.html', {})

def likeview(request, pk):
  post = get_object_or_404(Post, id =request.POST.get('post_id')) #post_id is nothing but the name = post_id in article detail
  liked = False
  if post.likes.filter(id =request.user.id).exists(): #from database if it exist remove it
     post.likes.remove(request.user) #after unliked like = false
     liked = False
  else:
    post.likes.add(request.user) # first time liking #we are showing who liked post so we use request.user
    liked = True
  return HttpResponseRedirect(reverse('detail', args=[str(pk)]))
  

class Home(ListView):
    model = Post
    template_name='homepage.html'
    ordering = ['-post_date']
    # ordering = ['-id'] #latest one default django set id

 
 #for the category drop down

# if we want that category nav dropdown menu in the detail page we have to mention this get context though
    def get_context_data(self, **kwargs):
        cats_menu = Category.objects.all() #passing all the categories into the category drop down nav bar
        context = super(Home, self).get_context_data(**kwargs)
        context["cat_menu"] = cats_menu #context variable to base
        return context
    
        

class ArticleDetailView(DetailView):
    model = Post
    template_name='article_detail.html'

# if we want that category nav dropdown menu in the detail page we have to mention this get context though
# we have specified {% if cat_menu %} exist then only so we are providing this menu here

    #for the category drop down
    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all() #passing all the categories into the category drop down nav bar
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

 # we are looking blog of 15 and we need to see the id of 15
        stuff = get_object_or_404(Post, id= self.kwargs['pk']) 
        total_likes = stuff.total_likes() #total_likes() from models

        # for dislike 
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked =True

        context["cat_menu"] = cats_menu #context variable to article_detail.html
        context['total_likes'] = total_likes #to article detail.html
        context['liked'] = liked #for disliked
        return context                                                                                         


class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = "__all__" #form will take care of the fields when we are adding form we dont have to mention fields
    #fields =["title", "body"] 

class AddCategoryView(CreateView):
    model = Category
    template_name ='add_category.html'
    fields = '__all__'

def categorylistview(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',{'cat_menu_list':cat_menu_list })


#creating a category page all the post in coding 
def categoryview(request, cats): #from urls  
    #replacing "-" with the ' ' slugify
    category_post = Post.objects.filter(category = cats.replace('-', ' ')) #model field category = particular category
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_post':category_post})



class ArticleUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html' 
    #form will take care of the fields when we are adding form we dont have to mention fields 
    #but we doesn't author to be edited in suchcase creating a editform will remove the author field in the EditForm
    # fields = ['title', 'title_tag', 'body']

class ArticleDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = "__all__"
    success_url = reverse_lazy('home')

# without this will get an NOT NULL constraint failed: blog_comment.post_id
    def form_valid(self, form):
# http://localhost:8000/article/1/comment in order to assign the 1 to the form which can be access by kwargs['pk]
        form.instance.post_id = self.kwargs['pk'] 
        return super().form_valid(form)
