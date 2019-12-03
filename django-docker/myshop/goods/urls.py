from django.urls import path

from goods.views import IndexView, DetailView, ListView
urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('goods/<sku_id>', DetailView.as_view(), name='detail'),
    path('list/<type_id>/<page>', ListView.as_view(), name='list'),
]
