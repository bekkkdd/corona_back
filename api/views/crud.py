# import json
#
# from django.http import JsonResponse
# from django.views import View
# from django.views.decorators.csrf import csrf_exempt
#
# from api.models import Country, Person
#
#
# @csrf_exempt
# def country_list(request):
#     if request.method == 'GET':
#         countries = Country.objects.all()
#         countries_json = [c.to_json() for c in countries]
#         return JsonResponse(countries_json, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         countries = Country.objects.create(name=data.get('name'))
#         return JsonResponse(countries.to_json())
#
#
# @csrf_exempt
# class CountryList(View):
#     def get(self, request):
#         countries = Country.objects.all()
#         countries_json = [c.to_json() for c in countries]
#         return JsonResponse(countries_json, safe=False)
#
#     def post(self, request):
#         data = json.loads(request.body)
#         countries = Country.objects.create(name=data.get('name'))
#         return JsonResponse(countries.to_json)
#
#
# @csrf_exempt
# def country_detail(request, country_id):
#     try:
#         country = Country.objects.get(id=country_id)
#     except Country.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#
#     if request.method == 'GET':
#         return JsonResponse(country.to_json())
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         country.name = data.get('name', country.name)
#         country.save()
#         return JsonResponse(country.to_json())
#     elif request.method == 'DELETE':
#         country.delete()
#         return JsonResponse({'deleted': True})
#
#
# @csrf_exempt
# class CountryDetails(View):
#     def get(self, request, country_id):
#         try:
#             country = Country.objects.get(id=country_id)
#         except Country.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
#         JsonResponse(country.to_json())
#
#     def put(self, request, country_id):
#         try:
#             country = Country.objects.get(id=country_id)
#             data = json.loads(request.body)
#             country.name = data.get('name', country.name)
#             country.save()
#             return JsonResponse(country.to_json())
#         except Country.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
#
#     def delete(self, request, country_id):
#         try:
#             country = Country.objects.get(id=country_id)
#             country.delete()
#             return JsonResponse({'deleted': True})
#         except Country.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
#
#
# @csrf_exempt
# def country_people(request, country_id):
#     if request.method == 'GET':
#         people = Person.objects.filter(country_id=country_id)
#         people_json = [c.to_json() for c in people]
#         return JsonResponse(people_json, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         people = Person.objects.create(name=data.get('name'))
#         return JsonResponse(people.to_json())
#
#
# @csrf_exempt
# class CountryPeople(View):
#     def get(self, request, country_id):
#         people = Person.objects.filter(country_id=country_id)
#         people_json = [c.to_json() for c in people]
#         return JsonResponse(people_json, safe=False)
#
#     def post(self, request, country_id):
#         data = json.loads(request.body)
#         people = Person.objects.create(name=data.get('name'))
#         return JsonResponse(people.to_json())
#
#
# @csrf_exempt
# def person_list(request):
#     if request.method == 'GET':
#         people = Person.objects.all()
#         people_json = [c.to_json() for c in people]
#         return JsonResponse(people_json, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         people = Person.objects.create(name=data.get('name'))
#         return JsonResponse(people.to_json())
#
#
# @csrf_exempt
# class PersonList(View):
#     def get(self, request):
#         people = Person.objects.all()
#         people_json = [c.to_json() for c in people]
#         return JsonResponse(people_json, safe=False)
#
#     def post(self, request):
#         data = json.loads(request.body)
#         people = Person.objects.create(name=data.get('name'))
#         return JsonResponse(people.to_json())
#
#
# @csrf_exempt
# def person_detail(request, person_id):
#     try:
#         person = Person.objects.get(id=person_id)
#     except Country.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#
#     if request.method == 'GET':
#         return JsonResponse(person.to_json())
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         person.name = data.get('name', person.name)
#         person.save()
#         return JsonResponse(person.to_json())
#     elif request.method == 'DELETE':
#         person.delete()
#         return JsonResponse({'deleted': True})
#
#
# @csrf_exempt
# class PersonDetails(View):
#     def get(self, request, person_id):
#         try:
#             person = Person.objects.get(id=person_id)
#             return JsonResponse(person.to_json())
#         except Country.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
#
#     def put(self, request, person_id):
#         try:
#             person = Person.objects.get(id=person_id)
#             data = json.loads(request.body)
#             person.name = data.get('name', person.name)
#             person.save()
#             return JsonResponse(person.to_json())
#         except Country.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
#
#     def delete(self, request, person_id):
#         try:
#             person = Person.objects.get(id=person_id)
#             person.delete()
#             return JsonResponse({'deleted': True})
#         except Country.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
