from django.test import TestCase
from django.contrib.auth.models import Permission, User, Group, ContentType
from workflow.models import Profile

class WorkflowModels(TestCase):
    def setUp(self):
        from website import initial_data

    def test_kent_profile(self):
        kent = Group.objects.all()[3].user_set.all()[0]
        kent.first_name = "Kent"
        kent.last_name = "Shikama"

        profile_kent = Profile(user=kent, position='photographer')
        self.assertEqual("Kent Shikama", profile_kent.display_name())