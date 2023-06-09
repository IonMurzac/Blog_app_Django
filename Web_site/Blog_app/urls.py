from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, CustomLoginView, RegisterPage, PostContact
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='posts'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('contact/', PostContact.as_view(), name='contact'),

    path('', PostList.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
    path('post-update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('post-delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)