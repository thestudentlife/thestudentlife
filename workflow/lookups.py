from ajax_select import LookupChannel
from workflow.models import Profile

class ProfileLookup(LookupChannel):
    model = Profile
    def get_query(self,q,request):
        return Profile.objects.filter(display_name__icontains=q).order_by('display_name')
    
