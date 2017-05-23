from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^user/(?P<user_id>[0-9]+)/$', views.get_user_permissions, name='get_user_permissions'),
    url(r'^checkpermission', views.checkpermission, name='checkpermission'),
    url(r'^permissions/(?P<permission_id>[0-9]+)/$', views.deletepermission, name='deletepermission'),
    url(r'^roles/(?P<role_id>[0-9]+)/$', views.update_permission, name='update_permission'),
    #url(r'^(?P<credit>\w+)&(?P<month>\w+)$', views.refinance_calculation, name='refinance_calculation'),
    #url(r'^cr', views.calculate, name="calculate" )
]

