from django.urls import path

from lawyers.views import signup, login, LawyerListView, GetUserInfoView

urlpatterns = [
    path('register/', signup, name='register_lawyer'),
    path('login/', login, name='login_lawyer'),
    path('lawyers/', LawyerListView.as_view(), name='lawyer-list'),
    path('token-auth/', GetUserInfoView.as_view(), name='token-auth'),
]
