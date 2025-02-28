from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet  # Ensure you import only views here

# Create a new router instance
customer_router = DefaultRouter()
customer_router.register(r'customers', CustomerViewSet, basename='customer')

# No need to import customer_router again
urlpatterns = customer_router.urls
