# -*- coding: utf-8 -*-
"""
django mail lib to support sending mass html mails
"""
from html2text import html2text

from django.utils.translation import ugettext as _
from django.core.mail import EmailMultiAlternatives, get_connection


def create_message(subject, message_plain, message_html, email_from, email_to,
                   custom_headers=None, attachments=None):
    """Build a multipart message containing a multipart alternative for text (plain, HTML) plus
    all the attached files.
    :param message_plain:
    :param message_html:
    :param email_from:
    :param email_to:
    :param custom_headers:
    :param attachments:
    :param subject:
    """
    if not message_plain and not message_html:
        raise ValueError(_('Either message_plain or message_html should be not None'))

    if not message_plain:
        message_plain = html2text(message_html)

    return {'subject': subject, 'body': message_plain, 'from_email': email_from, 'to': email_to,
            'attachments': attachments or (), 'headers': custom_headers or {}}


def send_mass_html_mail(datatuple):
    """send mass EmailMultiAlternatives emails
    :param datatuple:
    see: http://stackoverflow.com/questions/7583801/send-mass-emails-with-emailmultialternatives
    datatuple = ((subject, msg_plain, msg_html, email_from, email_to, custom_headers, attachments),)
    """
    connection = get_connection()
    messages = []
    for subject, message_plain, message_html, email_from, email_to,\
            custom_headers, attachments in datatuple:

        msg = EmailMultiAlternatives(
            **create_message(subject, message_plain, message_html, email_from, email_to,
                             custom_headers, attachments))
        if message_html:
            msg.attach_alternative(message_html, 'text/html')
        messages.append(msg)

    return connection.send_messages(messages)
