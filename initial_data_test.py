import django
django.setup()
from django.contrib.auth.models import Permission, User, Group, ContentType

kent = Group.objects.all()[3].user_set.all()[0]
print("username for kent: " + kent.username)
print("password for kent: " + kent.password)

ziqi = Group.objects.all()[3].user_set.all()[1]
print("username for ziqi: " + ziqi.username)
print("password for ziqi: " + ziqi.password)

latina = Group.objects.all()[3].user_set.all()[2]
print("username for latina: " + latina.username)
print("password for latina: " + latina.password)

goldPermissions = Group.objects.all()[3].permissions.all()
print("Gold Permissions:")
for index, permission in enumerate(goldPermissions):
    print("Gold Permission " + str(index) + ": " + permission.name)

print("End test")