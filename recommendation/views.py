import django_filters.rest_framework
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from drf_yasg.utils import swagger_auto_schema

from recommendation.serializers import *
from recommendation.models import *


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'username']

    @swagger_auto_schema(operation_summary='List all users')
    def list(self, request, *args, **kwargs):
        return super(self).list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Retrieve the user')
    def retrieve(self, request, *args, **kwargs):
        return super(self).retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Update the user')
    def update(self, request, *args, **kwargs):
        return super(self).update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Partially update the user')
    def partial_update(self, request, *args, **kwargs):
        return super(self).partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Destroy the user')
    def destroy(self, request, *args, **kwargs):
        return super(self).destroy(request, *args, **kwargs)

    @action(
        detail=False, methods=['get'],
        url_path='me/similar',
    )
    def similar(self, user_id):
        """Get users that are alike the given user

        Get users that are alike the given user
        """

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        detail=False, methods=['get', 'put', 'patch'],
        url_path='me',
    )
    def me(self, user_id):
        """Information about current user

        Information about current user
        """

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', ]

    @swagger_auto_schema(operation_summary='List all books')
    def list(self, request, *args, **kwargs):
        return super(self).list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Create a new book')
    def create(self, request, *args, **kwargs):
        return super(self).create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Retrieve the book')
    def retrieve(self, request, *args, **kwargs):
        return super(self).retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Update the book')
    def update(self, request, *args, **kwargs):
        return super(self).update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Partially update the book')
    def partial_update(self, request, *args, **kwargs):
        return super(self).partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Destroy the book')
    def destroy(self, request, *args, **kwargs):
        return super(self).destroy(request, *args, **kwargs)

    @action(
        detail=False, methods=['get'],
        url_path='recommendations_from/(?P<user_id>[^/.]+)',
    )
    def recommendations_from(self, user_id):
        """List books that are recommended by the given user

        List books that are recommended by the given user
        """

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        detail=False, methods=['get'],
        url_path='recommendations_to/(?P<user_id>[^/.]+)',
    )
    def recommendations_to(self, user_id):
        """List books that are recommended to the given user

        List books that are recommended to the given user
        """

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        detail=True, methods=['get'],
        url_path='similar',
    )
    def similar(self):
        """List books that are similar to the given one

        List books that are similar to the given one
        """

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['first_name', 'middle_name', 'last_name']


class ReviewViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['rating', 'book', 'reviewer']

    @swagger_auto_schema(operation_summary='List all reviews')
    def list(self, request, *args, **kwargs):
        return super(self).list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Create a new review')
    def create(self, request, *args, **kwargs):
        return super(self).create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Retrieve the review')
    def retrieve(self, request, *args, **kwargs):
        return super(self).retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Update the review')
    def update(self, request, *args, **kwargs):
        return super(self).update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Partially update the review')
    def partial_update(self, request, *args, **kwargs):
        return super(self).partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Destroy the review')
    def destroy(self, request, *args, **kwargs):
        return super(self).destroy(request, *args, **kwargs)

    @swagger_auto_schema(deprecated=True)
    @action(
        detail=False, methods=['get'],
        url_path='book/(?P<book_id>[^/.]+)'
    )
    def to_book(self, book_id):
        """Reviews given to the book

        Reviews given to the book
        """

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(deprecated=True)
    @action(
        detail=False, methods=['get'],
        url_path='user/(?P<user_id>[^/.]+)'
    )
    def from_user(self, user_id):
        """Reviews given by the user

        Reviews given by the user
        """

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
