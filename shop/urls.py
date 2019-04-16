from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.Index, name='Index'),
	 url(r'^list/$', views.ProductList, name='ProductList'),
	url(r'^post_list/$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
]
  

