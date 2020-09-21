from .views import HomeView,HomePageView,Detail_View
from django.urls import path


urlpatterns = [
    # path('',HomeView.as_view(),name='home'),
    path('',HomePageView.as_view(),name='home'),
    path('<int:pk>',Detail_View.as_view(),name='details')

]