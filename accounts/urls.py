from django.urls    import  path
from accounts.views import  userLogin


urlpatterns = [
    path("",userLogin,name="user-login"),
    # path('VerifyUser/<uidb64>/<token>/', Activation.as_view(), name="active")
]