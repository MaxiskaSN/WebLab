from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalog_all, name="catalog_all"),
    path('videocards/', views.videocards, name="videocards"),
    path('cpu/', views.cpu, name="cpu"),
    path('displays/', views.displays, name="displays"),
    path('videocards/<int:pk>', views.ProductDetailViewPrimary.as_view(), name='product-detail'),
    path('cpu/<int:pk>', views.ProductDetailViewSecondary.as_view(), name='product-detail-cpu'),
    path('displays/<int:pk>', views.ProductDetailViewTertiary.as_view(), name="product-detail-display")
]
