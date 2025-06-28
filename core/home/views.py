from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


@api_view(['GET', 'POST'])
def show(request):
    return Response({"Report": "Report finished"})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.all()

        if objs.exists():
            serializer = PersonSerializer(objs, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No people found"}, status=204)

    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        try:
            obj = Person.objects.get(id = data.get('id'))
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status = 404)
        serializer = PersonSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        try:
            obj = Person.objects.get(id = data.get('id'))
        except Person.DoesNotExist:
            return Response({'message': "Person not found"}, status = 404)
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    else:
        data = request.data
        try:
            obj = Person.objects.get(id = data['id'])
        except Person.DoesNotExist:
            return Response({"message": "Person not found"}, status=404)
        obj.delete()
        return Response({'message': "Person deleted"})








