from rest_framework.routers import DefaultRouter

from api.views import EmpleadosViewSet, EmpresasViewSet

router = DefaultRouter()

router.register(r'empresas', EmpresasViewSet, basename="empresas")
router.register(r'empleados', EmpleadosViewSet, basename="empleados")

urlpatterns = router.urls