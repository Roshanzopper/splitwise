from django.conf.urls import url, include
from MainApp import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'splituser', views.SplitUserList)
router.register(r'expensegroup', views.ExpenseGroupList)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', views.login, name='login'),
]
