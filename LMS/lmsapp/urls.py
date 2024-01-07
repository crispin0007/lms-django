from django.urls import path
from lmsapp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.home , name="home"),
    path('login/', views.login_view , name="login"),
    path('register/', views.register , name="register"),
    path('dashboard/', views.dashboard , name="dashboard"),
    path('profile/', views.profile , name="profile"),
   
    path('checkout/', views.checkout , name="checkout"),

    # ==========students urls========
    path('mylearning', views.mylearning , name="mylearning"),
    path('messages', views.messages , name="messages"),
    # path('notifications', views.notifications , name="notifications"),
    path('mycart', views.mycart , name="mycart"),
    path('settings', views.settings , name="settings"),
    path('wishlists', views.wishlists , name="wishlists"),
    path('becomeinstructor', views.becomeinstructor , name="becomeinstructor"),
    # path('purchase', views.purchase , name="purchase"),
]
