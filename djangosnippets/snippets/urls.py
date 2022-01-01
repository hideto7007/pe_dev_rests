from django.urls import path

from snippets import views

urlpatterns = [
    path("new/", views.snippet_new, name="snippet_new"),
    path("<int:snippet_id>/", views.snippet_detail, name="snippet_detail"),
    # path("<int:snippet_id>/comments/new", views.comment_new, name="comment_new"),  # comment追加
    path("<int:snippet_id>/edit/", views.snippet_edit, name="snippet_edit"),
]
