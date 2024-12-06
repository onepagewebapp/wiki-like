from django.urls import path
from . import views

urlpatterns = [
    # Homepage, listing all entries
    path("", views.index, name="index"),
    
    # View for a specific entry by its ID
    path("entry/<int:entry_id>/", views.entry_detail, name="entry_detail"),
    
    # Search results
    path("search_results/", views.search_results, name="search_results"),
    
    # Create new entry
    path("new/", views.new_page, name="new_page"),
    
    # Edit entry
    path("edit/<int:entry_id>/", views.edit_page, name="edit_page"),
    
    # Random page
    path("random/", views.random_page, name="random_page"),

    # Delete entry
    path("delete/<int:entry_id>/", views.delete_entry, name="delete_entry"),
    
    # 404 error page 
    #path("404/", views.page_not_found, name="page_not_found"),
]
