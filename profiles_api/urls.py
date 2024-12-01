from django.urls import path, include  # (including list of URLS)

from profiles_api import views

# For ViewSets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, base_name='hello-viewset') #Register specific viewsets with our router.
                                                                # can access api with hello-viewset, viewset registered
                                                                # base_name used to retrieve the URLs in our router using url retrieving function

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)) # When we register a router , it generates a list of urls that are associated with viewsets.
                                    # blank string specify means it don't use a prefix
]
