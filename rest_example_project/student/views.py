from rest_framework import viewsets
from .models import Student
from .serializers import StudientSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `checkBody` action.
    """
    queryset = Student.objects.all()
    serializer_class = StudientSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    test_param1 = openapi.Parameter('check_type', openapi.IN_QUERY, description="height or width", type=openapi.TYPE_STRING)
    test_param2 = openapi.Parameter('id', openapi.IN_QUERY, description="id of student", type=openapi.TYPE_NUMBER)
    user_response = openapi.Response('response description', StudientSerializer)

    @swagger_auto_schema(method='get', manual_parameters=[test_param1, test_param2], responses={404: 'Not found', 200:'ok', 201:StudientSerializer})
    @action(methods=['GET'], detail=False, url_path='check-body')
    def check_body(self, request):
        """
        Check body API
        """
        check_type = request.query_params.get('check_type')
        id = request.query_params.get('id')

        print(check_type, id)
        obj = self.queryset.get(id=id)
        rs = ""
        if check_type == 'height':
            if obj.height > 1:
                rs = "tall"
            else:
                rs = "short"
        else:
            if obj.weight > 1:
                rs = "fat"
            else:
                rs = "thin"
        return Response({"result": rs})

    # @action(methods=['POST'], detail=False)
    # def echo(self, request):
    #     # deserializer
    #     obj = StudientSerializer(request.data)
    #     print(obj)
    #     # serializer
    #     return Response(obj.data)

    # @action(methods=['GET'], detail=False)
    # def find_by_name(self, request):
    #     name = request.query_params.get('name')
    #     print(self.queryset)
    #     objs = Student.objects.filter(name__exact=name)
    #     return Response(StudientSerializer(objs).data)
