from .import settings
from django.conf.urls.static import static
from store import views as about_view 
from django.contrib.auth import views as auth_views 
from User_Accounts import views as log_views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/',auth_views.LoginView.as_view(template_name = 'User_Accounts/login.html'),name='login'),
    path('logout/',log_views.logout_view,name='logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name ='User_Accounts/password_reset.html'),
        name='password_reset'),
    path('password-reset-done/',
        auth_views.PasswordResetDoneView.as_view(template_name ='User_Accounts/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name ='User_Accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
     path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name ='User_Accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    path('',include('User_Accounts.urls')),
    
    path('about/',about_view.about,name='about'),
    path('',include(('store.urls', 'store'), namespace ='store')),
   
     path('cart/',include(('cart.urls', 'cart'), namespace ='cart')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
