from django.urls import path
from . import views

urlpatterns = [
    # path('search/', views.search_symbol, name='search_symbol'),
    # # Add other API URLs here
    # path('tsla/', views.get_tsla_data, name='tsla_data'),
    path('api/quote/', views.get_stock_quote, name='get_stock_quote'),

    path('api/stocks/', views.get_stock_list),
    path('search/', views.search_symbol, name='search_symbol'),
    path('stock/<str:stock_symbol>/', views.fetch_stock_details, name='fetch_stock_details'),
    path('quote/<str:stock_symbol>/', views.fetch_quote, name='fetch_quote'),
    path('historical/<str:stock_symbol>/<str:resolution>/<int:from_timestamp>/<int:to_timestamp>/', views.fetch_historical_data, name='fetch_historical_data'),
]
