from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views.cbv import CountryList, PersonList, CountryPeople, PersonDetails, CountryDetails, CountryRegions, \
    RegionDetails, CityDetails, RegionCities, CountryCities, RegionPeople, CityPeople
from api.views.fbv import country_list, region_list, city_list

urlpatterns = [

    path('login/', obtain_jwt_token),
    path('countries/', country_list),
    path('countries/<int:pk>/', CountryDetails.as_view()),

    path('regions/', region_list),
    path('countries/<int:country_id>/regions/', CountryRegions.as_view()),
    path('regions/<int:pk>/', RegionDetails.as_view()),

    path('regions/<int:region_id>/cities/', RegionCities.as_view()),
    path('cities/', city_list),
    path('cities/<int:pk>/', CityDetails.as_view()),
    path('countries/<int:country_id>/cities/', CountryCities.as_view()),

    path('countries/<int:country_id>/people/', CountryPeople.as_view()),
    path('regions/<int:region_id>/people/', RegionPeople.as_view()),
    path('cities/<int:city_id>/people/', CityPeople.as_view()),
    path('people/', PersonList.as_view()),
    path('people/<int:pk>/', PersonDetails.as_view())
]
