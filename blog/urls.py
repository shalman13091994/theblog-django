from django.urls import path
from .views import (Home,ArticleDetailView, ArticleCreateView,
ArticleUpdateView, ArticleDeleteView, AddCategoryView, categoryview,categorylistview, likeview,AddCommentView)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='detail' ),
    path('add_post/', ArticleCreateView.as_view(), name = 'create'),
    path('article/edit/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('article/<int:pk>/delete',ArticleDeleteView.as_view(), name='delete' ),
    path('add_category/', AddCategoryView.as_view(), name = 'category'),
    path('category/<str:cats>/', categoryview, name='category_view'),
    path('category-list/',categorylistview, name='category-list'),
    path('like/<int:pk>',likeview, name='like-post'),
      path('article/<int:pk>/comment', AddCommentView.as_view(), name = 'add_comment'),

]

