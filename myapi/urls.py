from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from api_core.views import UserViewSet, GroupViewSet, GroupUserViewSet, AgentViewSet
from api_logs.views import EventViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"agents", AgentViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"groupusers", GroupUserViewSet)
router.register(r"events", EventViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Central Erros",
        default_version='v1',
        description="Bem vindo a API Central de Erros",
        terms_of_service="",
        contact=openapi.Contact(email="camila.bodack@gmail.com"),
        license=openapi.License(name="API Central Erros"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),
]
