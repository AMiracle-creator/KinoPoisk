from uuid import uuid4

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from main.forms import RegForm, AuthForm, EditProfForm
from main.models import Comment, Movie, KinopoiskUser
from main.serializers import CommentSerializer, CreateCommentSerializer
from main.services import method_f, select, prefetch, valueList
from news.tasks import movies_count, change_password


def TestView(request):
    print(select().producer)

    print(prefetch())

    vl = valueList()
    print(vl)

    print(method_f())
    return render(request, 'main/test.html')


def reset_password(request, user_id, token):
    context = {
        'user_id': user_id,
        'token': token,
    }
    if request.method == 'GET':
        return render(request, 'main/reset_password.html', context)
    elif request.method == 'POST':
        if request.POST['password'] == request.POST['rep_password']:
            KinopoiskUser.objects.filter(id=user_id).update(password=make_password(request.POST['password']))
            return redirect('login')
        return render(request, 'main/reset_password.html', context)


def success_email(request):
    if request.method == 'GET':
        return render(request, 'main/success_send_email.html')


def forgot_password(request):
    if request.method == 'GET':
        return render(request, 'main/email_confirmation.html')
    elif request.method == 'POST':
        user = KinopoiskUser.objects.get(email=request.POST['email'])
        if user:
            print(request.POST['email'])
            token = uuid4()
            change_password(user.id, token)
            return redirect('send_email')
        else:
            return render(request, 'main/email_confirmation.html')


class RegistrationView(CreateView):
    form_class = RegForm
    success_url = reverse_lazy('authPage')
    template_name = 'main/registration.html'


def auth_view(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is None:

                error = 'Неправильный логин или пароль'
                context = {'error': error}

                return render(request, 'registration.html', context)

            else:
                login(request, user)
                return redirect('home')

    context = {'error': ''}

    return render(request, 'main/auth.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()


    else:
        form = EditProfForm(instance=request.user)

    return render(request, 'main/redactProfile.html', {'form': form})


class AuthenticatedPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.id == request.user.id


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, movie_id=None, *args, **kwargs):
        comments = Comment.objects.filter(movie=movie_id)
        if comments:
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        else:
            return Response(status=200)

    def create(self, request, movie_id=None, *args, **kwargs):
        serializer = CreateCommentSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data='success')
        return Response(status=403, data='failure')

    def update(self, request, movie_id=None, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.get_object().id)
        comment.text = request.data['text']
        comment.save()
        return Response(status=203, data='update')

    def destroy(self, request, movie_id=None, *args, **kwargs):
        Comment.objects.filter(id=self.get_object().id).delete()

        return Response(status=203, data='success')

    # @action('')
    # def movie(self, request, *args, **kwargs):


def logout_view(request):
    logout(request)
    return redirect('authPage')


def home_page(request):
    return render(request, 'main/index.html')


class AboutPage(TemplateView):
    template_name = "main/about.html"


class AllFilmsPage(ListView):
    model = Movie
    template_name = 'main/allFilms.html'


def login_page(request):
    return render(request, 'main/login.html')


@login_required
def profile_page(request, id):
    return render(request, 'main/profile.html')


def profile_films(request):
    return render(request, 'main/profileFilms.html')


class SingleFilmView(DetailView):
    model = Movie
    template_name = 'main/singleFilm.html'


def contacts(request):
    return render(request, 'main/contact.html')
