from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    CreateLicense,
    CreatePlateNumber,
    Dashboard, 
    LicenseDetail, 
    Index, 
    LicenseListView, 
    ListPlateNumber, 
    Registration,
    SearchResult
)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('signup/', Registration.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('search/', SearchResult.as_view(), name='search'),

 
    # ----------------- [ Drive's license] ----------------------
    path('license/detail/<uuid:pk>/', LicenseDetail.as_view(), name='driver_license_detail'),
    path('license-list/', LicenseListView.as_view(), name='license'),
    path('add-license/', CreateLicense.as_view(), name='add_license'),

    # -------------- [ plate number urls ] -------------------
    path('platenumber/list/', ListPlateNumber.as_view(), name='list_platenumber'),
    path('platenumber/create/', CreatePlateNumber.as_view(), name='create_platenumber'),
    
]
