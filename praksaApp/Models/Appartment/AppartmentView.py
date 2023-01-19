# from AppartmentModel import Appartment
# from AppartmentSerializer import AppartmentSerializer
# from django.db.models import query
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework import status, mixins, generics

# @api_view(['GET', 'POST'])
# def AppartmentList(request):
#     query = Appartment.objects.all()
#     serializer_class = AppartmentSerializer(query, many = True)
#     return Response(serializer_class.data)

# class ListAppartments(APIView):
#     def get(self, request):
#         query = Appartment.objects.all()
#         serializer_class = AppartmentSerializer(query, many = True)
#         return Response(serializer_class.data)
    
#     def post(self, request):
#         serializer_obj = AppartmentSerializer(data = request.data)
#         if serializer_obj.is_valid(raise_exception=True):
#             appartment_saved = serializer_obj.save()
#             return Response({"Success": "Appartment '{}' created successfully".format(appartment_saved)})
#         return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class AppartmentDetailedView(APIView):
#     def get(self, request, id):
#          query = Appartment.objects.filter(appartmentId=id)
#          serializer_class = AppartmentSerializer(query, many = True)