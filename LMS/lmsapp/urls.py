from django.urls import path, include
from lmsapp import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.auth.models import User


urlpatterns = [
    
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.home , name="home"),
    path('accounts/login/', views.login_view , name="login"),
    path('register/', views.register , name="register"),
    path('dashboard/', views.dashboard , name="dashboard"),
    path('verify/<str:token>', views.verify , name="verify"),
    path('profile/', views.profile , name="profile"),   
    path('checkout/<slug:slug>/', views.checkout , name="checkout"),    
    path('blog/', views.blog , name="blog"),
    
    
    # ==========students urls========
    # path('messages/', views.messages, name="messages"),   
    path('learning_area/<slug:slug>/', views.learning_area, name="learning_area"),
    path('notifications/', views.notifications , name="notifications"),

   

    #details with slug url
    path('course_details/<slug:slug>/', views.course_details , name="coursedetails"),
    path('blog_details/<slug:slug>/', views.course_details , name="blogdetails"),
    path('edit_course/<slug:slug>/', views.edit_course , name="editcourse"),
    path('accounts/details/<slug:slug>/', views.account_details , name="accdetails"),
    path('edit_blog/<slug:slug>/', views.edit_blog , name="editblog"),

    # update urls
    path('update_profile/', views.update_profile, name='update_profile'),
    path('update_course/<int:course_id>', views.update_course, name='update_course'),
    path('update_blog/<int:blog_id>', views.update_blog, name='update_blog'),

    #delete urls
    
    path('delete_course/<int:course_id>', views.delete_course, name='delete_course'),
    path('delete_blog/<int:blog_id>', views.delete_blog, name='delete_blog'),

    #publish urls
    path('publish_course/<int:course_id>', views.publish_course, name='publish_course'),
    path('unpublish_course/<int:course_id>', views.unpublish_course, name='unpublish_course'),
    path('approve_instructor/<int:user_id>', views.approve_instructor, name='approve_instructor'),
    path('publish_blog/<int:blog_id>', views.publish_blog, name='publish_blog'),
    path('unpublish_blog/<int:blog_id>', views.unpublish_blog, name='unpublish_blog'),
    path('unapprove_instructor/<int:user_id>', views.unapprove_instructor, name='unapprove_instructor'),
    path('request_instructor/<int:user_id>', views.request_instructor, name='request_instructor'),


    path('cart/<slug:slug>/', views.cart , name="cart"),
    path('settings/', views.settings , name="settings"),
    path('wishlists/', views.wishlists , name="wishlists"),
    path('becomeinstructor/', views.becomeinstructor , name="becomeinstructor"),
    path('purchasehistory/', views.purchasehistory , name="purchasehistory"),
    path('myfeedbacks/', views.myfeedbacks , name="myfeedbacks"),

    #new item adding
    path('addcourse/', views.addcourse , name="addcourse"),  
    path('addblog/', views.addblog , name="addblog"),
    path('myblogs/', views.myblogs , name="myblogs"),
    path('mycourses/', views.mycourses , name="mycourses"),

    #new blog course adding urls
    path('create_course/', views.create_course , name="create_course"),  
    path('create_blog/', views.create_blog , name="create_blog"),

    path('blog_status_function/<int:blog_id>/', views.blog_status_function, name='blog_status_function'),
    path('course_status_function/<int:course_id>/', views.course_status_function, name='course_status_function'),

    #lesson urls
    path('add_lesson/<int:course_id>', views.add_lesson, name='add_lesson'),
    path('add_lesson_name/<int:course_id>', views.add_lesson_name, name='add_lesson_name'),
    path('add_lesson_name/<int:course_id>', views.add_lesson_name, name='add_lesson_name'),
    path('add_chapter/<int:lesson_id>', views.add_chapter, name='add_chapter'),
    #social Login
    path('auth/', include('social_django.urls', namespace='social')),

    # Approval
    path('approval_course/', views.approval_course , name="approval_course"),
    path('approval_blog/', views.approval_blog , name="approval_blog"),
    path('approval_instructor/', views.approval_instructor , name="approval_instructor"),

    # Lists
    path('list_course/', views.list_course , name="list_course"),
    path('list_blog/', views.list_blog , name="list_blog"),
    path('list_instructor/', views.list_instructor , name="list_instructor"),
    path('list_student/', views.list_student , name="list_student"),

    # Income
    path('total_income/', views.total_income , name="total_income"),
    path('all_feedbacks/', views.all_feedbacks , name="all_feedbacks"),
    path('top_course/', views.top_course , name="top_course"),

    #  path('test/', views.test , name="test"),
     path('khalti-response/', views.khalti_response , name="khalti-response"),
    #function_urls

    path('send/<int:receiver_id>/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),


    path('search/', views.search_query, name='search_query'),
    path('generate-certificate/', views.generate_certificate, name='generate_certificate'),

    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

