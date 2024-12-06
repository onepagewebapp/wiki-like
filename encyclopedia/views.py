from . import util
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewPageForm, EditPageForm
from .models import Entry
import random
import markdown2

def index(request):
    entries = Entry.objects.all()  
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    html_content = markdown2.markdown(entry.content)
    return render(request, 'encyclopedia/entry_detail.html', {
        "entry": entry,
        "title": entry.title,
        "content": html_content
    })

def search_results(request):
    query = request.GET.get('q', '')
    results = Entry.objects.filter(title__icontains=query)

    if results.exists():
        return render(request, "encyclopedia/search_results.html", {
            "results": results,
            "title": "Search Results"
        })
    else:
        return render(request, "encyclopedia/404.html", {"message": "Entry not found"})

def new_page(request):
    form = NewPageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'encyclopedia/new_page.html', {'form': form})

def edit_page(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    form = EditPageForm(request.POST or None, instance=entry)

    if form.is_valid():
        form.save()
        return redirect("entry_detail", entry_id=entry.id)

    return render(request, 'encyclopedia/edit_page.html', {'form': form})


#def random_page(request):
    #entries = Entry.objects.all()
    #random_entry = random.choice(entries)
    #return render(request, 'encyclopedia/random_page.html', {"entry": random_entry})

def random_page(request):
    entries = Entry.objects.all()
    random_entry = random.choice(entries)
    
    # Convert the markdown content to HTML
    html_content = markdown2.markdown(random_entry.title) 

    return render(request, 'encyclopedia/random_page.html', 
    {"entry": random_entry, "html_content": html_content})


def delete_entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry.delete()
    return redirect('index')

