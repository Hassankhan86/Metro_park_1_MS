from django.contrib import admin
from django.urls import path, include
from dashboard import views as dashboard
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from metropark import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard.homepage),
    # path('form',dashboard.form)
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),

    # path('dashboard/',include('dashboard.urls')),
    # path('accounts/', include('accounts.urls')),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

