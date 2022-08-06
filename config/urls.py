from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .settings import VERSION

schema_view = get_schema_view(
    openapi.Info(
        title="U-T-A -  API System",
        default_version=f"{VERSION}",
        description="API REST using django and U-T-A",
        contact=openapi.Contact(email="aguileraa18@gmail.com"),
        license=openapi.License(name="AAAB Industries"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.home.urls")),
    path("", include("apps.authentication.urls")),
    path(
        f'{VERSION}/docs/',
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
