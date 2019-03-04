
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('admin/rosetta/', include('rosetta.urls')),
    path('', include(('apps.shop.urls', "shop"), namespace='shop')),
    path(_('blog/'), include(('apps.blog.urls', "blog"), namespace='blog')),
    path(_('contact/'), include(('apps.contact.urls', "contact"), namespace='contact')),
    prefix_default_language=False
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
