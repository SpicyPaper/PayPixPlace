from django.urls import path, include
from .views import CanvasView, CanvasDetailsView
from . import views

urlpatterns = [
    path('', views.home, name='paypixplace-home'),
    path('canvas/create/', views.createCanvas, name='canvas-create'),
    path('canvas/official/', views.officialCanvas, name='canvas-official'),
    path('canvas/community/', CanvasView.as_view(), name='canvas-community'),
    path('canvas/user/', views.userCanvas, name='canvas-user'),
    path('canvas/<int:pk>/', CanvasDetailsView.as_view(), name='canvas-detail'),
    path('canvas/<int:id>/json/', views.get_json, name='canvas-json'),
    path('canvas/<int:id>/img/', views.get_img, name='canvas-img'),
    path('change_pixel_color/', views.change_pixel_color, name='change-pixel-color'),
    path('change_user_slot_color/', views.change_user_slot_color, name='change_user_slot_color'),
    path('pix/purchase/', views.purchase, name='pix-purchase'),
    path('pix/purchase/<int:id>/', views.payment, name='pix-payment'),
    path('buy/<int:id>', views.buy_with_pix, name='buy-element'),
]