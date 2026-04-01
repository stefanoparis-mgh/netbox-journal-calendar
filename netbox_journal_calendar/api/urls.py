from netbox.api.routers import NetBoxRouter
from .. import views


router = NetBoxRouter()
router.register('journal-icon-configs', views.JournalIconConfigViewSet)


urlpatterns = router.urls