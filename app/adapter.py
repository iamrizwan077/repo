# from allauth.account.adapter import DefaultAccountAdapter


# class CustomAccountAdapter(DefaultAccountAdapter):

#     def save_user(self, request, user, form, commit=False):
#         user = super().save_user(request, user, form, commit)
#         data = form.cleaned_data
#         user.user_type = data.get('role')
#         user.save()
#         return user

from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        user_field(user, 'role', request.data.get('role', ''))
        user_field(user, 'department', request.data.get('department', ''))
        user.save()
        return user