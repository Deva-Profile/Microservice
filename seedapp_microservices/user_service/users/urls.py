from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', SignupUserAPI.as_view(), name='signup'),
    path('login/', LoginUserAPI.as_view(), name='login'),
    path('logout/', LogoutUserAPI.as_view(), name='logout'),]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)