from .models import UserLsn24


def validator(email, password):
    user = UserLsn24.objects.get(email=email)
    if user.password == password:
        return True


def hide_email():
    users = UserLsn24.objects.all().order_by('-id')
    hide_emails = []
    for u in users:
        hide_emails.append(u.email[:2] + (u.email.index('@') - 2) * '*' + u.email[u.email.index('@'):])
    return hide_emails
