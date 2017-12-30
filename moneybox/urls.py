from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from saver import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'algorithms', views.AlgorithmViewSet)
router.register(r'distributions', views.DistributionViewSet)
router.register(r'savers', views.SaverViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'liabilities', views.LiabilityViewSet)
router.register(r'assets', views.AssetViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/api-token-auth/', obtain_jwt_token),
    url(r'^admin/', admin.site.urls),
    # url(r'^', views.AppView.as_view()),
]
