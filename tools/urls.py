from django.urls import path
from . import views

urlpatterns = [
        path("", views.home_view,name="home page"),
        path("<str:name>", views.tool_view, name="tool page"),
        path("<str:name>/status/<str:status>", views.tool_status_update, name="update_tool_status"),
        path("<str:name>/maintained",views.tool_maintained, name="maintain_tool")
        ]
