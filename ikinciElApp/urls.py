from django.conf.urls import url
from ikinciElApp.views import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^home/$', HomePageView.as_view(), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', RegistrationView.as_view(), name='signup'),
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'^addproduct/$',ProductCreateView.as_view(), name='addproduct'),
    url(r'^productlist/$',ProductView.as_view(), name='productlist'),
    url(r'^basket/$',views.basket_list, name='basket'),
    url(r'^buy/(?P<id>\d+)/$',views.buy_product, name ='buy'),
    url(r'^basket/(?P<id>\d+)/$',views.addToBasket, name='basket'),
    url(r'^userlist/$',UserListView.as_view(), name='userlist'),
]
