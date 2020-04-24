from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views.cbv import CountryList, PersonList, CountryPeople, PersonDetails, CountryDetails, CountryRegions, \
    RegionDetails, CityDetails, RegionCities, CountryCities, RegionPeople, CityPeople
from api.views.fbv import country_list, region_list, city_list, country_detail, region_detail, city_detail, person_list, \
    person_detail, message_list_by_user_id

urlpatterns = [

    path('login/', obtain_jwt_token),
    path('countries/', country_list),
    path('countries/<int:pk>/', country_detail),

    path('regions/', region_list),
    path('countries/<int:country_id>/regions/', CountryRegions.as_view()),
    path('regions/<int:pk>/', region_detail),

    path('regions/<int:region_id>/cities/', RegionCities.as_view()),
    path('cities/', city_list),
    path('cities/<int:pk>/', city_detail),
    path('countries/<int:country_id>/cities/', CountryCities.as_view()),

    path('countries/<int:country_id>/people/', CountryPeople.as_view()),
    path('regions/<int:region_id>/people/', RegionPeople.as_view()),
    path('cities/<int:city_id>/people/', CityPeople.as_view()),
    path('people/', person_list),
    path('people/<int:pk>/', person_detail),

    path('message/', message_list_by_user_id)
]
