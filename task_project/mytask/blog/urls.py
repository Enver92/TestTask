from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name="comment_remove"),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^profile/$', views.update_profile, name='update_profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
