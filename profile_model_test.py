import django
django.setup()

from django.contrib.auth.models import Permission, User, Group, ContentType
from workflow.models import Profile

kent = Group.objects.all()[2].user_set.all()[0]
kent.first_name = "Kent"
kent.last_name = "Shikama"

profile_kent = Profile(user=kent, position='photographer')
print("Full name: " + profile_kent.display_name())