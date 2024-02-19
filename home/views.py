# views.py

from django.shortcuts import render
from .models import Person
from django.utils.html import format_html


def search_view(request):
    all_people = Person.objects.all()
    context = {'count': all_people.count()}
    return render(request, 'search.html', context)


def search_results_view(request):
    query = request.GET.get('search', '')
    print(f'{query = }')

    all_people = Person.objects.all()
    if query:
        people = all_people.filter(name__icontains=query)
        highlighted_people = [{'name': highlight_matched_text(person.name, query), 'description': person.description}
                              for person in people]
    else:
        highlighted_people = []

    context = {'people': highlighted_people, 'count': all_people.count()}
    return render(request, 'search_results.html', context)


def highlight_matched_text(text, query):
    """
    Inserts html around the matched text.
    """
    start = text.lower().find(query.lower())
    if start == -1:
        return text
    end = start + len(query)
    highlighted = format_html('<span class="highlight">{}</span>', text[start:end])
    return format_html('{}{}{}', text[:start], highlighted, text[end:])
