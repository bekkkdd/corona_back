from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views.cbv import CountryList, PersonList, CountryPeople, PersonDetails, CountryDetails
from api.views.fbv import country_list


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('countries/', country_list),
    path('countries/<int:pk>/', CountryDetails.as_view()),
    path('countries/<int:country_id>/people/', CountryPeople.as_view()),
    path('people/', PersonList.as_view()),
    path('people/<int:pk>/', PersonDetails.as_view())
]

