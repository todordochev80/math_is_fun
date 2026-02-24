from django.shortcuts import render, get_object_or_404, redirect
from players.models import Player, Score
from django.db.models import Count, Sum


def practice_progress_view(request):
    player_id = request.session.get('current_player_id')

    if not player_id or not Player.objects.exists():
        return redirect('player_list')

    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        return redirect('player_list')

    stats = Score.objects.filter(player=player).values('operation_type').annotate(
        total_solved=Count('id'),
        total_points=Sum('score')
    )

    total_stars = stats.aggregate(Sum('total_points'))['total_points__sum'] or 0

    return render(request, 'progress/practice.html', {
        'player': player,
        'stats': stats,
        'total_stars': total_stars,
    })