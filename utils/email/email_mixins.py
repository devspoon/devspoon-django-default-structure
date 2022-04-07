import uuid
import hashlib

from django.urls import reverse

from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from typing import NoReturn, Tuple, Union

# from minitutorial import settings
from django.conf import settings

from django.core.mail import send_mail
from django.template.loader import render_to_string

class VerifyEmailMixin:
    email_template_name = '/email/registration_verification.html'
    token_generator = default_token_generator

    def send_verification_email_management(self, template: str, sender: str, user: object, email_vendor_code: int = 1, token_gen_type: int = 1 ) -> NoReturn:
        if template is not None:
            email_template_name = template

        if token_gen_type is 1:
            # use default_token_generator
            self.__create_verification_email_generator(sender, user)
        else :
            # use custom token generator
            self.__create_verification_email_custom_token(self, sender, user)


    def __create_verification_email_generator_token(self, sender, user: object) -> HttpResponse:
        token = self.token_generator.make_token(user)
        url = self.__build_verification_link(user, token)

        subject = '회원가입을 축하드립니다.'
        message = '다음 주소로 이동하셔서 인증하세요. {}'.format(url)
        html_message = render(self.request, self.email_template_name, {'url': url}).content.decode('utf-8')
        send_mail(subject, message, sender, [user.email], html_message, fail_silently=True) # fail_silently=false, failure notification


    def __build_verification_link(self, user, token) -> str:
        return '{}/user/{}/verify/{}/'.format(self.request.META.get('HTTP_ORIGIN'), user.pk, token)


    def __create_email_key(user_id) -> NoReturn:
        random_key = str(uuid.uuid4())
        sha_data = hashlib.sha256()
        sha_data.update(str(user_id).encode('utf-8'))
        hash_key = sha_data.hexdigest()

        return random_key[::2] + hash_key[::2]


    def __create_verification_email_custom_token(self, sender, user) -> NoReturn:
        key = self.__create_email_key(user.id)
        link = 'http://' + self.request.get_host() + reverse('verification') + '?key=' + key

        # expired_at = timezone.now() + timedelta(days=3)
        # UserVerification.objects.create(user=user, key=key, expired_at=expired_at)

        email_context = { 'link': link }
        msg_plain = render_to_string('email/verification.txt', email_context)
        msg_html = render_to_string('email/verification.html', email_context)

        subject = '회원가입을 축하드립니다. 이메일 인증을 완료해 주세요'
        send_mail(
            subject, 
            msg_plain,
            sender,
            [user.email],
            html_message=msg_html,
            fail_silently=True
        )
