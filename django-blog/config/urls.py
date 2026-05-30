from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_redirect, name="login_redirect"),
    path("home/", views.home, name="home"),
    path("update/", views.update, name="update"),
    path("comment/<int:post_id>/", views.add_comment, name="add_comment"),
    path("search/", views.search_profile, name="search_profile"),
    path("register/", views.register, name="register"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("logout/", views.LogoutPage.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
