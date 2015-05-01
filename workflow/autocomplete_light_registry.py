import autocomplete_light
from workflow.models import Profile

class ProfileAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^display_name',]
    model = Profile
autocomplete_light.register(Profile, ProfileAutocomplete)