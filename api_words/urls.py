from django.urls import path

from .views import QuoteAPIView
from .views import QuoteCategoryAPIView
from .views import QuoteAPIDetailView
from .views import QuoteAPINewView

urlpatterns = [
    path('', QuoteCategoryAPIView.as_view()),
    path('word/', QuoteAPIView.as_view()),
    path('word/<int:pk>/', QuoteAPIDetailView.as_view()),
    path('word/new/', QuoteAPINewView.as_view()),
]