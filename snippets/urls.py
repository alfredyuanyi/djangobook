from django.conf.urls import url
from snippets import views
from snippets import articleView
from snippets import topSchoolViews
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    url(r'^article/$', articleView.articleList),
    #url(r'^article/(?P<pk>[0-9]+)/$', articleView.articleDetail),
    url(r'^article/link/', articleView.articleDetail),

    url(r'^newsnippets/$', views.SnippetList.as_view()),
    url(r'^newsnippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^newarticle/$', articleView.article_list.as_view()),
    url(r'^newarticle/link/(?P<pk>[0-9]+)/$', articleView.article_detail.as_view()),

    url(r'topschool/register/$', topSchoolViews.register),
    url(r'topschool/login/$', topSchoolViews.login),
    url(r'topschool/setconcerndirection/$', topSchoolViews.setconcerndirection),
    url(r'topschool/test/$', topSchoolViews.test),
]
urlpatterns = format_suffix_patterns(urlpatterns)