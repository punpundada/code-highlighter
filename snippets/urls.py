from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("snippets/",view=views.SnippetListView.as_view(),name="Snippets_list"),
    path("snippets/<int:pk>/",view=views.snippetDetailsView.as_view(),name="snippet_details"),
    path("snippets/<int:pk>/highlighted/",view=views.SnippetHighlighted.as_view(),name="snippet_highlighted"),
    path("user/",view=views.UserListView.as_view(),name="user_list"),
    path("user/<int:pk>/",view=views.UserDetailsView.as_view(),name="user_details"),
    path("",view=views.api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)

