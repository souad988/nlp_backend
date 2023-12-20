from django.urls import path
from .views import DocumentUploadAPIView

urlpatterns = [
    path('upload', DocumentUploadAPIView.as_view(), name='document_upload'),
    # Other URL patterns if needed
]
