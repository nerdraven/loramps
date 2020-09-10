from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework import routers
from apps.views import api, events, auth, tickets


events_urls_patterns = [
    path('', events.EventsAPI.as_view()),
    path('<int:pk>', events.EventAPI.as_view()),
    path('<int:id>/tickets/', events.tickets),
    path('<int:id>/tickets/<int:ticket>', events.ticket),
]


tickets_urls_patterns = [
    path('', tickets.TicketListAPI.as_view()),
    path('<int:pk>', tickets.TicketAPI.as_view()),
]


auth_urls_patterns = [
    path('login', auth.LoginAPI.as_view()),
    path('register', auth.RegisterAPI.as_view()),
    path('users', auth.UserAPI.as_view()),
]

api_extras_patterns = [
    path('choices', api.choices),
]


schema = get_schema_view(
    title='Users API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)


urlpatterns = [
    path('', api.index),
    path('admin/', admin.site.urls),
    path('api/docs', include_docs_urls(title='Ticket System API')),
    path('api/extras/', include(api_extras_patterns)),
    path('api/auth/', include(auth_urls_patterns)),
    path('api/events/', include(events_urls_patterns)),
    path('api/tickets/', include(tickets_urls_patterns)),
    path('api/schema', schema),
]