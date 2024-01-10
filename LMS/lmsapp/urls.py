from django.urls import path, include
from lmsapp import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    # path('', include(tf_urls)),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.home , name="home"),
    path('accounts/login/', views.login_view , name="login"),
    path('register/', views.register , name="register"),
    path('dashboard/', views.dashboard , name="dashboard"),
    path('verify/<str:token>', views.verify , name="verify"),
    path('profile/', views.profile , name="profile"),   
    path('checkout/<slug:slug>/', views.checkout , name="checkout"),
    path('course_details/<slug:slug>/', views.course_details , name="coursedetails"),
    path('blog/', views.blog , name="blog"),
    path('edit_course/<slug:slug>/', views.edit_course , name="editcourse"),
    path('edit_blog/<slug:slug>/', views.edit_blog , name="editblog"),

    # ==========students urls========
    path('mycourses/', views.mycourses , name="mycourses"),
    path('messages/', views.messages , name="messages"),
    path('notifications/', views.notifications , name="notifications"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('cart/<slug:slug>/', views.cart , name="cart"),
    path('settings/', views.settings , name="settings"),
    path('wishlists/', views.wishlists , name="wishlists"),
    path('becomeinstructor/', views.becomeinstructor , name="becomeinstructor"),
    path('purchasehistory/', views.purchasehistory , name="purchasehistory"),
    path('myfeedbacks/', views.myfeedbacks , name="myfeedbacks"),
    path('addcourse/', views.addcourse , name="addcourse"),
    path('addblog/', views.addblog , name="addblog"),
    path('myblogs/', views.myblogs , name="myblogs"),

    path('auth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
