from django.urls import path,include
from app.views import register, login_view,home_view,account_view,search_bills,add_bill,statistics_view,delete_bill,edit_bill_view,predict_expenses,export_bill
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from app.views import UserViewSet
from django.conf.urls.static import static
from django.conf import settings
router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('home', home_view, name='home'),
    path('account', account_view, name='account'),
    path('search/', search_bills, name='search'),
    path('add/', add_bill, name='add_bill'),
    path('thongke/', statistics_view, name='thongke'),
    path('delete-bill/<int:bill_id>/', delete_bill, name='delete_bill'),
    path('api/', include(router.urls)),
    path('edit-bill/<int:bill_id>/', edit_bill_view, name='edit_bill'),
    path('predict/', predict_expenses, name='predict'),
    path('export-bill/<int:bill_id>/', export_bill, name='export_bill'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
