from django.urls import path
from .views import PollingUnitResultsView, SummedLGAResultsView, AddPollingUnitResultsView

urlpatterns = [
    path('polling-unit/<int:uniqueid>/', PollingUnitResultsView.as_view(), name='polling-unit-results'),
    path('lga/<int:lga_id>/results/', SummedLGAResultsView.as_view(), name='summed-lga-results'),
    path('polling-unit/results/', AddPollingUnitResultsView.as_view(), name='add-polling-unit-results'),
]