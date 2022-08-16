from rest_framework import viewsets
from .models import Student
from .serializers import StudientSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import StaticHTMLRenderer
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

    @action(methods=['GET'], detail=False, url_path='check-body')
    def check_body(self, request):
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
        return Response({"result":rs})
    
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