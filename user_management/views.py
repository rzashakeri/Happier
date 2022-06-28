# # Register User Separate steps
# class SignupWizard(SessionWizardView):
#     form_list = [
#         SignupFormStepOne,
#         SignupFormStepTwo,
#         SignupFormStepThree,
#         SignupFormStepFour,
#         SignupFormStepFive,
#     ]
#
#     def done(self, form_list, **kwargs):
#         first_name = form_list[0].cleaned_data["first_name"]
#         last_name = form_list[1].cleaned_data["last_name"]
#         username = form_list[2].cleaned_data["username"]
#         email = form_list[3].cleaned_data["email"]
#         password = form_list[4].cleaned_data["password1"]
#         user = User(
#             first_name=first_name, last_name=last_name, username=username, email=email
#         )
#         user.set_password(password)
#         user.save()
#         complete_signup(
#             self.request,
#             user,
#             settings.ACCOUNT_EMAIL_VERIFICATION,
#             settings.LOGIN_REDIRECT_URL,
#         )
#         return render(self.request, "account/verification_sent.html")
