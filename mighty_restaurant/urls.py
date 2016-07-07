from django.conf.urls import url, include
from django.contrib import admin

from app.views import IndexView, KitchenView, ServerView, OwnerView, ProfilePageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^kitchen/$', KitchenView.as_view(), name="kitchen_view"),
    url(r'^server/$', ServerView.as_view(), name="server_view"),
    url(r'^owner/$', OwnerView.as_view(), name="owner_view"),
    url(r'^accounts/profile/$', ProfilePageView.as_view(), name="profile_page_view")
]
