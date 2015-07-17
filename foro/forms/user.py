# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.template import defaultfilters
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

User = get_user_model()


class RegistrationForm(UserCreationForm):

    honeypot = forms.CharField(label=_("Leave blank"), required=False)

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Elije un nombre de usuario'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Crea una contraseña'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'}))

    class Meta:
        model = User
        fields = ("username", "email")
        widgets = {
            "email": forms.TextInput(attrs={'placeholder': 'Tu correo'})
        }

    def clean_honeypot(self):
        """Check that nothing's been entered into the honeypot."""
        value = self.cleaned_data["honeypot"]

        if value:
            raise forms.ValidationError(_("Do not fill this field."))

        return value

    def clean_username(self):
        # Override
        username = self.cleaned_data["username"]

        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError(_("The username is taken."))

    def save(self, commit=True):
        self.instance.is_active = False
        return super(RegistrationForm, self).save(commit)


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "bio", "company", "web_site",
                  "linkedin_url", "github_username",  "trello_username")

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu usuario'}), max_length=254)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Tu contraseña'}))


class EmailChangeForm(forms.Form):

    email = forms.CharField(label=_("Email"), widget=forms.EmailInput)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data["password"]

        if not self.user.check_password(password):
            raise forms.ValidationError(_("Your password was entered incorrectly. "
                                          "Please enter it again."))

        return password

    def clean_email(self):
        email = self.cleaned_data["email"]

        if email == self.user.email:
            raise forms.ValidationError(_("Try a different email."))

        return email

    def get_email(self):
        return self.cleaned_data["email"]


class ResendActivationForm(forms.Form):

    email = forms.CharField(label=_("Email"), widget=forms.EmailInput)

    def clean_email(self):
        email = self.cleaned_data["email"]

        try:
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(_("The provided email does not exists."))

        if self.user.last_ip:
            raise forms.ValidationError(_("This account was activated."))

        return email

    def get_user(self):
        return self.user


class PasswordResetForm(forms.Form):

    email = forms.EmailField(label=_("Email"), max_length=254)

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.
        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        active_users = get_user_model()._default_manager.filter(
            email__iexact=email, is_active=True)
        return (u for u in active_users if u.has_usable_password())

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            return email
        else:
            raise forms.ValidationError(u'El correo "%s" no esta asociado a un usuario registrado' % email)

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        email = self.cleaned_data["email"]
        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            context = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }

            self.send_mail(subject_template_name, email_template_name,
                           context, from_email, user.email,
                           html_email_template_name=html_email_template_name)
