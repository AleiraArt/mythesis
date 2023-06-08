from django.shortcuts import render

def badges(request):
    context = {
        'played_iliad': request.session.get('played_iliad', False),
        'played_pride_and_prejudice': request.session.get('played_pride_and_prejudice', False),
        'played_three_musketeers': request.session.get('played_three_musketeers', False),
        'played_war_and_peace': request.session.get('played_war_and_peace', False),
        'played_hound_baskervilles': request.session.get('played_hound_baskervilles', False),
    }
    return render(request, 'badges/badges.html', context)
