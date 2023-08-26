from django.shortcuts import get_object_or_404
from djoser import views
from rest_framework import response, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import Follow, User
from .serializers import UserSerializer, UserWithReceptSerializer


class UserViewSet(views.UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(
        detail=False, methods=["get"],
        permission_classes=[IsAuthenticated],
    )
    def subscriptions(self, request):
        users = User.objects.filter(followers__subscriber=request.user).all()
        page = self.paginate_queryset(users)
        serializer = UserWithReceptSerializer(
            page, many=True, context={"request": self.request}
        )

        return self.get_paginated_response(serializer.data)

    @action(
        detail=True, methods=["post", "delete"],
        permission_classes=[IsAuthenticated]
    )
    def subscribe(self, request, id):
        author = get_object_or_404(User, id=id)

        if request.user == author:
            return response.Response(
                "Cant subscribe on yourself",
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.method == "POST":
            if not Follow.objects.filter(
                author=author, subscriber=request.user
            ).exists():
                Follow.objects.create(author=author, subscriber=request.user)
                serializer = UserWithReceptSerializer(
                    author, context={"request": self.request}
                )
                return response.Response(serializer.data)

            return response.Response(
                "Already subscribed", status=status.HTTP_400_BAD_REQUEST
            )

        if request.method == "DELETE":
            follow = get_object_or_404(
                Follow, subscriber=request.user, author=author
            )
            follow.delete()
            return response.Response("Success")
