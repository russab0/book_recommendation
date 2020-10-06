from rest_framework.routers import DefaultRouter

from recommendation.views import *

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'books', BookViewSet, basename='books')
# router.register(r'author', AuthorViewSet, basename='authors')
router.register(r'reviews', ReviewViewSet, basename='reviews')

urlpatterns = router.urls
