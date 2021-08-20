from django import forms
from .models import Post, Category, comment

# creating a bootstrap designed form
# choices = [('coding', 'coding'), ('sports','sports'), ('entertainment', 'entertainment')] #hardcoded

#dynamic one takes from db
choices = Category.objects.all().values_list('name','name')

#from db to list (we just adding query to list to avoid the query set)
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm): #using the model from which we used in the database
    
    class Meta:
        model = Post
        fields = ("title",'title_tag','author','category','body', 'header_image')

        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'enter title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # using this id we can get to know who has logged in so we use id for javascript in the add_post.html
            'author': forms.TextInput(attrs={'class': 'form-control', 'value' :' ','id':'elder', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
#after adding the new category in the database restart the server

#we are mentioning the edit form inorder to remove the author field in the editpage


class EditForm(forms.ModelForm): #using the model from which we used in the database
    
    class Meta:
        model = Post
        fields = ("title",'title_tag','category','body')

        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'enter your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm): #using the model from which we used in the database
    
    class Meta:
        model = comment
        fields = ('name','body')

        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
