from django.urls import path
from . import views

urlpatterns = [
    path('contents/', views.ContentsView.as_view()),
    path('contents/<int:content_id>', views.ContentsById.as_view()),
    path('contents/filter/', views.FilteredContents.as_view())
]