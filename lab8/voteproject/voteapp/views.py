from django.shortcuts import render
from .models import Vote
from django.db.models import Count

def vote_view(request):
    if request.method == 'POST':
        selected_choice = request.POST.get('choice')
        if selected_choice:
            Vote.objects.create(choice=selected_choice)

    total_votes = Vote.objects.count()
    results = Vote.objects.values('choice').annotate(count=Count('choice'))

    percentages = {
        'Good': 0,
        'Satisfactory': 0,
        'Bad': 0
    }

    if total_votes > 0:
        for result in results:
            percentages[result['choice']] = round(
                (result['count'] / total_votes) * 100, 2
            )

    context = {
        'percentages': percentages,
        'total_votes': total_votes
    }

    return render(request, 'voteapp/vote.html', context)