
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from schedule.views import BotUserListRetrieve, DocumentViewSet, GroupViewSet, ScheduleViewSet, GetBotUserView
from .schema import swagger_urlpatterns

router = DefaultRouter()
router.register('group', GroupViewSet)
router.register("document", DocumentViewSet)
router.register("schedule", ScheduleViewSet)
router.register("botuser", BotUserListRetrieve)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getuser/<str:full_name>/', GetBotUserView.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns+=router.urls
urlpatterns += swagger_urlpatterns
