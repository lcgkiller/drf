from django.conf.urls import url
from snippets import views

urlpatterns = [
        # url(r'^$', views.snippet_list),
        # url(r'^(?P<pk>\d+)/$', views.snippet_detail)

    # 클래스 기반 뷰
    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),

]