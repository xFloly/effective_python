from notes.views import NoteListView, NoteDetailView, NoteCreate, NoteUpdate, NoteDelete, TopicDetailView,TopicCreate,TopicUpdate,TopicDelete,TopicListView
from django.urls import path

app_name = "notes"

urlpatterns = [
    path("", NoteListView.as_view(), name='note-list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/add/', NoteCreate.as_view(), name='note-add'),
    path('note/<int:pk>/', NoteUpdate.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),
    path("topic/", TopicListView.as_view(), name='topic-list'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topic/add/', TopicCreate.as_view(), name='topic-add'),
    path('topic/<int:pk>/update', TopicUpdate.as_view(), name='topic-update'),
    path('topic/<int:pk>/delete/', TopicDelete.as_view(), name='topic-delete'),
]