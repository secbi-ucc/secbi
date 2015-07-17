# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.views import login as login_view
from django.contrib.auth.views import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from foro.utils.ratelimit.decorators import ratelimit
from foro.utils.user.email import send_activation_email, send_email_change_email
from foro.utils.user.tokens import UserActivationTokenGenerator, UserEmailChangeTokenGenerator


from ..models.topic import Topic
from ..models.comment import Comment

from ..forms.user import UserProfileForm, RegistrationForm, LoginForm, EmailChangeForm, ResendActivationForm, PasswordResetForm


User = get_user_model()


@ratelimit(field='username', rate='5/5s')
def custom_login(request, **kwargs):
    # Current Django 1.5 login view does not redirect somewhere if the user is logged in
    if request.user.is_authenticated():
        return redirect(request.GET.get('next', request.user.get_absolute_url()))

    if request.is_limited and request.method == "POST":
        return redirect(request.get_full_path())

    return login_view(request, authentication_form=LoginForm, **kwargs)


def custom_logout(request, **kwargs):
    # Current Django 1.6 uses GET to log out
    if not request.user.is_authenticated():
        return redirect(request.GET.get('next', reverse('foro:user-login')))

    if request.method == 'POST':
        return logout(request, **kwargs)

    return render(request, 'foro/user/logout.html')

@csrf_protect
def custom_reset_password(request, is_admin_site=False,
                   template_name='foro/user/password_reset_form.html',
                   email_template_name='foro/user/password_reset_email.html',
                   subject_template_name='foro/user/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   current_app=None,
                   extra_context=None,
                   html_email_template_name=None):
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
            }
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': _('Password reset'),
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


@ratelimit(rate='2/10s')
def register(request):
    if request.user.is_authenticated():
        return redirect(request.GET.get('next', reverse('foro:profile-update')))

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)

        if not request.is_limited and form.is_valid():
            user = form.save()
            send_activation_email(request, user)
            messages.info(request, _("Te hemos enviado un correo electrónico para que pueda activar su cuenta!!"))

            # TODO: email-less activation
            # if not settings.REGISTER_EMAIL_ACTIVATION_REQUIRED:
            # login(request, user)
            # return redirect(request.GET.get('next', reverse('foro:profile-update')))

            return redirect(reverse('foro:user-login'))
    else:
        form = RegistrationForm()

    return render(request, 'foro/user/register.html', {'form': form, })


def registration_activation(request, pk, token):
    user = get_object_or_404(User, pk=pk)
    activation = UserActivationTokenGenerator()

    if activation.is_valid(user, token):
        user.is_active = True
        user.save()
        messages.info(request, _("Tu cuenta ha sido activada!"))

    return redirect(reverse('foro:user-login'))


@ratelimit(field='email', rate='5/5m')
def resend_activation_email(request):
    if request.user.is_authenticated():
        return redirect(request.GET.get('next', reverse('foro:profile-update')))

    if request.method == 'POST':
        form = ResendActivationForm(data=request.POST)

        if not request.is_limited and form.is_valid():
            user = form.get_user()
            send_activation_email(request, user)

        messages.info(request, _("Si usted no recibe un correo electrónico, por favor asegúrese de que ha introducido"
                                 "la dirección que se registró, y comprobar su carpeta de correo no deseado."))
        return redirect(reverse('foro:user-login'))
    else:
        form = ResendActivationForm()

    return render(request, 'foro/user/activation_resend.html', {'form': form, })


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, _("Tu pefil se actualizo!"))
            return redirect(reverse('foro:profile-update'))
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'foro/user/profile_update.html', {'form': form, })


@login_required
def profile_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, _("Tu contrasena fue cambiada!"))
            return redirect(reverse('foro:profile-update'))
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'foro/user/profile_password_change.html', {'form': form, })


@login_required
def profile_email_change(request):
    if request.method == 'POST':
        form = EmailChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            send_email_change_email(request, request.user, form.get_email())
            messages.info(request, _("Te hemos enviado un email para que confirmes los cambios!"))
            return redirect(reverse('foro:profile-update'))
    else:
        form = EmailChangeForm()

    return render(request, 'foro/user/profile_email_change.html', {'form': form, })


@login_required
def email_change_confirm(request, token):
    user = request.user
    email_change = UserEmailChangeTokenGenerator()

    if email_change.is_valid(user, token):
        user.email = email_change.get_email()
        user.save()
        messages.info(request, _("Tu email se cambio!"))

    return redirect(reverse('foro:profile-update'))


@login_required
def profile_topics(request, pk, slug):
    p_user = get_object_or_404(User, pk=pk)

    if p_user.slug != slug:
        return HttpResponsePermanentRedirect(reverse("foro:profile-topics", kwargs={'pk': p_user.pk,
                                                                                      'slug': p_user.slug}))

    topics = Topic.objects.for_public().filter(user=p_user).order_by('-date').select_related('user')

    return render(request, 'foro/user/profile_topics.html', {'p_user': p_user, 'topics': topics})


@login_required
def profile_comments(request, pk, slug):
    p_user = get_object_or_404(User, pk=pk)

    if p_user.slug != slug:
        return HttpResponsePermanentRedirect(reverse("foro:profile-detail", kwargs={'pk': p_user.pk,
                                                                                      'slug': p_user.slug}))

    comments = Comment.objects.for_user_public(user=p_user)
    return render(request, 'foro/user/profile_comments.html', {'p_user': p_user, 'comments': comments})


@login_required
def profile_likes(request, pk, slug):
    p_user = get_object_or_404(User, pk=pk)

    if p_user.slug != slug:
        return HttpResponsePermanentRedirect(reverse("foro:profile-likes", kwargs={'pk': p_user.pk,
                                                                                     'slug': p_user.slug}))

    comments = Comment.objects.for_public().filter(comment_likes__user=p_user).order_by('-comment_likes__date')
    return render(request, 'foro/user/profile_likes.html', {'p_user': p_user, 'comments': comments})


@login_required
def user_menu(request):
    return render(request, 'foro/user/menu.html')
