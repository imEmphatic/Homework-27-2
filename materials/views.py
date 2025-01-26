from rest_framework import generics, permissions, viewsets

from .models import Course, Lesson
from .permissions import IsModerator, IsOwner, IsOwnerOrModerator, ReadOnlyForAll
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            permission_classes = [permissions.IsAuthenticated & ~IsModerator]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsOwner | IsModerator]
        else:
            permission_classes = [ReadOnlyForAll | IsOwner | IsModerator]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = [permissions.IsAuthenticated & ~IsModerator]
        else:
            permission_classes = [ReadOnlyForAll | IsOwner | IsModerator]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            permission_classes = [IsOwner | IsModerator]
        else:
            permission_classes = [ReadOnlyForAll | IsOwner | IsModerator]
        return [permission() for permission in permission_classes]
