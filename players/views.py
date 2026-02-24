from django.db.models import Sum
from django.shortcuts import redirect
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
    template_name = 'players/scoreboard.html'
    context_object_name = 'top_players'

    def get_queryset(self):
        return Player.objects.annotate(
            total_stars=Sum('scores__score')
        ).order_by('-total_stars')


def select_player(request, player_id):
    request.session['current_player_id'] = player_id
    return redirect('math_operations', child_id=player_id)