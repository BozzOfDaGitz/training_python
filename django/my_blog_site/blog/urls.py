from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.UpdatePostView, name='post_update'),
    path('post/<int:pk>/delete/', views.DeletePostView, name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('about/', views.AboutView.as_view(), name='about'),
]
