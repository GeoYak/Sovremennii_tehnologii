from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ServiceApp.models import ServiceModel
from ServiceApp.serializers import ServiceSerializer


# Create your views here.


@csrf_exempt
def serviceApi(request, id=0):
    if request.method == 'GET':
        services = ServiceModel.objects.all()
        services_serializer = ServiceSerializer(services, many=True)
        return JsonResponse(services_serializer.data, safe=False)
    elif request.method == 'POST':
        service_data = JSONParser().parse(request)
        services_serializer = ServiceSerializer(data=service_data)
        if services_serializer.is_valid():
            services_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        service_data = JSONParser().parse(request)
        service = ServiceModel.objects.get(id=service_data['id'])
        services_serializer = ServiceSerializer(service, data=service_data)
        if services_serializer.is_valid():
            services_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        service = ServiceModel.objects.get(id=id)
        service.delete()
        return JsonResponse("Deleted Successfully", safe=False)
