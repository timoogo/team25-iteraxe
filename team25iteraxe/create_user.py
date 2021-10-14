from django.contrib.auth import get_user_model

# see ref. below
UserModel = get_user_model()

if not UserModel.objects.filter(username='admin').exists():
    user=UserModel.objects.create_user('admin', password='123')
    user.is_superuser=True
    user.is_staff=True
    user.save()

if not UserModel.objects.filter(username='Loyd').exists():
    user=UserModel.objects.create_user('Loyd', password='SDR567')
    user.is_superuser=False
    user.first_name = 'Loyd'
    user.last_name = 'Dupinpin'
    user.is_staff=True
    user.save()