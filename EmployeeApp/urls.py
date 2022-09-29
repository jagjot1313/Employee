from django.urls import path
from . import views

urlpatterns = [
    path('',views.openIndexPage),
    path('employee-form',views.openEmployeeForm),
    path('save-employee',views.saveEmployee),
    path('employees-list',views.getAllEmployees),
    path('remove-employee/<int:id>',views.removeEmployee),
    path('edit-employee/<int:id>',views.editEmployee),
    path('update-employee/<int:id>',views.updateEmployee)
]