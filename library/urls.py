from django.urls import path
from . import views
app_name='library'
urlpatterns =[
    path('', views.home, name='home'),
    path('book/',views.book,name='book'),
    path('book_details/<book_id>/',views.book_details,name='book_details'),
    path('book_edit/<int:book_id>',views.book_edit,name='book_edit'),
    path('book_delete/<int:book_id>',views.book_delete,name='book_delete'),
    path('update/<int:book_id>',views.update,name='update'),
    path('author/',views.author_view,name='author_view'),
    path('addbook/',views.add_book,name='add_book'),
    path('books/',views.add_submit,name='add_submit'),
    #__________user Interface_________________#
   
    path('signup/',views.signup_view,name='signup'),
    path('signin/',views.signup,name='signin'),
    path('login/',views.login_view,name='login'),
    path('loginin/',views.login,name='loginin'),
    
    
]