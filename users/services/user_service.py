from django.contrib.auth.models import User


def get_users():
    return User.objects.all()

def create_user(data):
    print(f'{data.__dict__}')
    user = User(username=data.username)
    user.set_password(user.password)
    user.save()
    return {'message': 'OK', 'data': data}