from django.db import router
from django.urls import path,include
from rest_framework.viewsets import ViewSet
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('productcart',viewset=views.ProductCartApi)
router.register('order',viewset=views.OrderApi)


urlpatterns = [
    path('',include(router.urls))
]

