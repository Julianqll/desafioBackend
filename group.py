import os
import django

# Configura la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import Group, User

# Define los nombres de los grupos
GROUPS = ['Admin', 'Colocador', 'Aprobador']

# Define los usuarios a crear con su respectivo grupo
USERS = [
    {'username': 'user1', 'password': 'password1', 'groups': ['Admin']},
    {'username': 'user2', 'password': 'password2', 'groups': ['Colocador']},
    {'username': 'user3', 'password': 'password3', 'groups': ['Aprobador']},
    # Agrega más usuarios si es necesario
]

# Crea los grupos
for group_name in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group_name)

# Crea los usuarios y los asigna a los grupos correspondientes
for user_data in USERS:
    username = user_data['username']
    password = user_data['password']
    groups = user_data['groups']
    
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()
        for group_name in groups:
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
        print(f'User {username} created successfully and added to groups: {groups}')
    else:
        print(f'User {username} already exists')

# Crear el superusuario y asignarlo a un grupo específico
superuser_data = {'username': 'admin', 'password': 'admin123', 'groups': ['Admin']}
superuser = User.objects.create_superuser(username=superuser_data['username'], email='admin@example.com', password=superuser_data['password'])
for group_name in superuser_data['groups']:
    group = Group.objects.get(name=group_name)
    superuser.groups.add(group)
print(f'Superuser {superuser.username} created successfully and added to groups: {superuser_data["groups"]}')

