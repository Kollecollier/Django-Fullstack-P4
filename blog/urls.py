
"""
URL paths to render view's to the browser.
"""

from .import views
from django.urls import path

urlpatterns = [
    path('', views.Postlist.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/update/', views.post_update, name='post_update'),
    path('<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('remove-comment/<slug>/', views.remove_comment, name='remove-comment'),
    path('update-comment/<slug>', views.update_comment, name='update-comment')

]
