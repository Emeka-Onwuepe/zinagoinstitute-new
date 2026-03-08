from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',include("frontview.urls" , namespace='frontview')),
    path('admin/', admin.site.urls),
]

urlpatterns+=staticfiles_urlpatterns()

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'errortemplate.views.page_not_found'
# handler403 = 'errortemplate.views.permission_denied'
# handler400 = 'errortemplate.views.bad_request'