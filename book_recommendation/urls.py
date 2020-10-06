from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_registration.api.views import login, register

schema_view = get_schema_view(
    openapi.Info(
        title="Book recommendation service API",
        default_version='v1',
        description="""
        Interface of a book recommendation service
        **Annotation type**: OAS editor.swagger.io
        **Api type**: HTTP REST
        **Author**: Ruslan Sabirov""",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="r.sabirov@innopolis.ru"),
        license=openapi.License(name="BSD License"),
    ),
    url='https://127.0.0.1/api/v1/',
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    path('', include('recommendation.urls')),

    url('authentication/login', login, name='login'),
    url('authentication/registration', register, name='registration'),
]
