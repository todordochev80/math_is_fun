from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from players.models import Player
from players.forms import PlayerForm

class PlayerListView(ListView):
    model = Player
    template_name = 'players/player_list.html'
    context_object_name = 'players'

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_form.html'
    success_url = reverse_lazy('player_list')

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_form.html'
    success_url = reverse_lazy('player_list')

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'players/player_confirm_delete.html'
    success_url = reverse_lazy('player_list')


class ScoreboardView(ListView):
    model = Player
    template_name = 'scoreboard.html'
    context_object_name = 'top_players'
    def get_queryset(self):
        ranked_players = Player.objects.all().order_by('-name')
        return ranked_players


