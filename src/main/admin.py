from django.contrib import admin

from main.models import Movie, KinopoiskUser, Producer, Comment, Review, Tag


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "production_year")
    ordering = ("production_year",)
    list_filter = ("production_year", "producer",)
    search_fields = ("name__startswith",)


@admin.register(KinopoiskUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name")
    list_filter = ("name", "birth_date",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)