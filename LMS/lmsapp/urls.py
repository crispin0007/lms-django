from django.urls import path
from lmsapp import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.home , name="home"),
    path('accounts/login/', views.login_view , name="login"),
    path('register/', views.register , name="register"),
    path('dashboard/', views.dashboard , name="dashboard"),
    path('verify/<str:token>', views.verify , name="verify"),
    path('profile/', views.profile , name="profile"),   
    path('checkout/', views.checkout , name="checkout"),
    path('course_details/', views.coursedetails , name="coursedetails"),
    path('blog/', views.blog , name="blog"),

    # ==========students urls========
    path('mylearning', views.mylearning , name="mylearning"),
    path('messages', views.messages , name="messages"),
    path('notifications', views.notifications , name="notifications"),
    path('update_profile', views.update_profile, name='update_profile'),
    path('mycart', views.mycart , name="mycart"),
    path('settings', views.settings , name="settings"),
    path('wishlists', views.wishlists , name="wishlists"),
    path('becomeinstructor', views.becomeinstructor , name="becomeinstructor"),
    # path('purchase', views.purchase , name="purchase"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
