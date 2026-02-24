from django.shortcuts import render

def index_page(request):
    player_id = request.session.get('current_player_id')
    return render(request, 'index_page.html', {
        'current_player_id': player_id
    })

