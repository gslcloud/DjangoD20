from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import CharacterCustomizationForm
from .models import CharacterClass


# Base class for character customization
class CharacterCustomizationView(View):
    template_name = 'character_customization.html'
    form_class = CharacterCustomizationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Create the character object and save it to the database
            character = form.save(commit=False)
            character.player = request.user
            character.save()
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})


# Customization view for each character class
class WarriorCustomizationView(CharacterCustomizationView):
    template_name = 'warrior_customization.html'


class WizardCustomizationView(CharacterCustomizationView):
    template_name = 'wizard_customization.html'


class RogueCustomizationView(CharacterCustomizationView):
    template_name = 'rogue_customization.html'