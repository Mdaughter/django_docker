from django.urls import path
from order.views import OrderPlaceView, OrderCommitView, CommentView

urlpatterns = [
    path('place', OrderPlaceView.as_view(), name='place'),
    path('commit', OrderCommitView.as_view(), name='commit'),
    #path(r'^pay$', OrderPayView.as_view(), name='pay'), # 订单支付
    #path(r'^check$', OrderCheckView.as_view(), name='check'), # 订单交易结果
    path('comment/<order_id>', CommentView.as_view(), name='comment'),
]