
from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'marker', views.marker, name='marker'),
        url(r'product', views.product, name='product'),
        url(r'init_main', views.init_main, name='init_main'),
        url(r'init_dist', views.init_dist, name='init_dist'),
        url(r'districts', views.districts, name='districts'),
        url(r'indDistricts', views.indDistricts, name='indDistricts'),
        url(r'region/(?P<district>([A-Z])\w+(\s)?(([A-Z])\w+)?(\s)?(([A-Z])\w+)?)', views.region, name='regions'),
        url(r'sms', views.sms, name='sms'),
        url(r'changedate', views.changedate, name='changedate'),
        url(r'addcases', views.addcases, name='addcases'),
        url(r'hosp_overview', views.hosp_overview, name='hosp_overview'),
        url(r'hellotest', views.hellotest, name='hellotest')
    ]
