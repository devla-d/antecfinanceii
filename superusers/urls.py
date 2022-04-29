from django.urls import path
from . import views





urlpatterns = [ 
    
    path('superuser/dashboard/',views.dashboard_view,name="super_dashboard"),
    path('superuser/users/',views.users_view,name="users"),
    path('superuser/user/<int:pk>/', views.user_detail_view, name="user-detail"),
    path('superuser/deposit/',views.deposit_view,name="superdeposit"),
    path('superuser/deposit/<int:pk>/',views.deposit_detail_view,name="superdeposit_detail"),
    path('superuser/withdrawals/',views.withdraw_view,name="superwithdrawals"),
    path('superuser/withdrawals/<int:pk>/',views.withdraw_detail_view,name="superwithdrawals_detail"),


    path('superuser/investments/',views.investmets_,name="investmenst_"),

    path('superuser/investments/<int:pk>/', views.investmets_details, name="investment-detail"),

     path('superuser/packages/',views.packages_,name="packages_"),








]