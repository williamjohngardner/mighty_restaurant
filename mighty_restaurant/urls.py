


from django.conf.urls import url, include
from django.contrib import admin

from app.views import IndexView, KitchenView, ServerView, OwnerView, ProfilePageView, CreateOrderView, OrderListView, OrderDetailView, DisplayOrderView, CreateOrderNumber


urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^kitchen/$', KitchenView.as_view(), name="kitchen_view"),
    url(r'^server/$', ServerView.as_view(), name="server_view"),
    url(r'^owner/$', OwnerView.as_view(), name="owner_view"),
    url(r'^accounts/profile/$', ProfilePageView.as_view(), name="profile_page_view"),
    url(r'^create_order/$', CreateOrderView.as_view(), name="create_order_view"),
    url(r'^create_order_number/$', CreateOrderNumber.as_view(), name="create_order_number"),
    url(r'^display_order/$', DisplayOrderView.as_view(), name="display_order_view"),
    url(r'^orders/$', OrderListView.as_view(), name="order_list_view"),
    url(r'^orders/(?P<pk>\d+)$', OrderDetailView.as_view(), name="order_detail_view")
]
