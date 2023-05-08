from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path("news", News, name="news"),
    path("news_deleted/<int:pk>/", News_deleted, name="news_deleted"),
    path("news_finished/<int:pk>/", News_finished, name="news_finished"),
    path("deleted_finished/<int:pk>/", Deleted_finished, name="deleted_finished"),
    path("finished_deleted/<int:pk>/", Finished_deleted, name="finished_deleted"),
    path("finished/", Finished, name="finished"),
    path("deleted/", Deleted, name="deleted"),
    path("bot/", Bot_views, name="bot"),
    path("add_bot/", Add_Bot, name="add_bot"),
    path("delete_bot/<int:pk>/", Delete_Bot, name="delete_bot"),
    path("bot_detail/", BotDetail_views, name="bot_detail"),
    path("add_bot_detail/", Add_BotDeteil, name="add_bot_detail"),
    path("delete_bot_detail/<int:pk>/", Delete_BotDetail, name="delete_bot_detail"),
    path("delete_science/<int:pk>/", DeleteScience, name="delete_science"),
    path("add_science/", AddScience, name="add_science"),
    path("science/", Science_view, name="science"),
]