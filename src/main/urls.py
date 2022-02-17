from django.conf.urls import url
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import SimpleRouter

from .views import auth_view, home_page, login_page, \
    profile_page, profile_films, edit_profile, contacts, logout_view, AboutPage, RegistrationView, \
    AllFilmsPage, TestView, SingleFilmView, forgot_password, success_email, reset_password

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="drf_kinopoisk",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

# router = SimpleRouter()
# router.register("comment", )

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('allFilms/', AllFilmsPage.as_view(), name='allFilms'),
    path('authPage/', auth_view, name='authPage'),
    path('login_page/', login_page, name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profileFilms/', profile_films, name='profileFilms'),
    path('profileRedact/', edit_profile, name='editProfile'),
    path('singlefilm/<int:pk>/', SingleFilmView.as_view(), name='singleFilm'),
    path('contacts/', contacts, name='contacts'),
    re_path(r'profile/(?P<id>\w+)/', profile_page, name="profile"),
    path('logout/', logout_view, name='logout'),
    re_path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('test/', TestView, name='test'),
    path('email_confirmation/', forgot_password, name='email_confirmation'),
    path('success_email/', success_email, name='send_email'),
    path('reset_password/<int:user_id>/<str:token>', reset_password, name='reset_password')
]
