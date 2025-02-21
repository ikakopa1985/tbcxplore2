from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User



class CardViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    def create(self, request, *args, **kwargs):
        user_id = request.data.get("user")
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)  # ✅ მომხმარებელი ხელით მივაკუთვნოთ
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
