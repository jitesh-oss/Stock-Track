# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from stock_track import views

urlpatterns = [

    # Stock Track
    path('add/', views.stock_input, name='add'),
    path('edit/', views.stock_edit, name='edit'),
    path('view/', views.stock_view, name='view'),
    path('nse-search/', views.nseStockSearch, name='nse-search'),
    path('bse-search/', views.bseStockSearch, name='bse-search'),
    path('nse-price/', views.nseStockPrice, name='nse-price'),
    path('bse-price/', views.bseStockPrice, name='bse-price'),
    path('fut-price/', views.futStockPrice, name='fut-price'),
    path('stock-delete/', views.stockDelete, name='stock-delete'),
    path('stocks-all/', views.stocksAll, name='stocks-all'),
    path('refresh-price/', views.refreshPrice, name='refresh-price'),
    path('refresh-stocktrack/', views.refreshStockTrack, name='refresh-stocktrack'),
    path('status-stocktrack/', views.statusStockTrack, name='status-stocktrack'),
    path('edit/<int:stock_id>/', views.stockEdit, name='stocks-edit'),

    # Stock Alerts
    path('alerts/add/', views.alert_input, name='alert-add'),
    path('alerts/view/', views.alert_view, name='alert-view'),
    path('alerts/alerts-all/', views.alertsAll, name='alerts-all'),
    path('alerts/refresh-alert/', views.refreshAlert, name='refresh-alert'),
    path('alerts/edit/', views.alert_edit, name='alert-edit'),
    path('alerts/alert-delete/', views.alertDelete, name='alert-delete'),
    path('alerts/refresh-allalerts/', views.refreshallAlerts, name='refresh-allalerts'),
    path('alerts/status-alerts/', views.statusAlerts, name='status-alerts'),

    # Stock Journal
    path('journal/category/', views.category_journal, name='category-journal'),
    path('journal/category-table/', views.category_journal_table, name='category-table'),
    path('journal/category-delete/', views.categoryDelete, name='category-delete'),
    path('journal/add/', views.journal_input, name='journal-add'),
    path('journal/view/', views.journal_view_all, name='journal-view'),
    path('journal/view/<int:jou_id>/', views.journal_edit_one, name='journal-editone'),
    path('journal/view/journal-delete/', views.journalDelete, name='journal-delete'),
    path('journal/view/one', views.journal_view_one, name='journal-viewone'),

]
