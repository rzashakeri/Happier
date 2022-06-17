from django.urls import path

from .forms import (
    SignupFormStepOne,
    SignupFormStepTwo,
    SignupFormStepThree,
    SignupFormStepFour,
    SignupFormStepFive,
)
from .views import SignupWizard

# Register User Separate steps
urlpatterns = [
    path(
        "register/",
        SignupWizard.as_view(
            [
                SignupFormStepOne,
                SignupFormStepTwo,
                SignupFormStepThree,
                SignupFormStepFour,
                SignupFormStepFive,
            ]
        ),
    ),
]
