from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.landing, name='landing'),
    url('^projects', views.projects, name='projects'),
    url('^addproject',views.postprojects,name="postprojects"),
    url('^profile', views.profile, name='profile'),
    url('^editdp', views.editdp, name='editdp'),
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^api/project/$',views.ProjectList.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
