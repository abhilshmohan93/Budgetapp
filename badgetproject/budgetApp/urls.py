from django.urls import path
from budgetApp.views import *


urlpatterns = [
    path('Registration/', Registration.as_view(), name="register_user"),
    path('Registration/Login', Login.as_view(), name="login_user"),
    path('Logout', logout.as_view(), name="logout_user"),
    path('Registration/Home', Home.as_view(), name="home"),
    path('CreateExpense/', CreateExpense.as_view(), name="create_expense"),
    path('ListExpense/', ListExpense.as_view(), name="list_expense"),
    path('AddCategory/', AddExpenseCat.as_view(), name="add_category"),
    path('DateExpencesum/', CalculateSumDate.as_view(), name="date_sum"),
    path('Categorysum/', CalculateSumCateg.as_view(), name="cat_sum"),
]