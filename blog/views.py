from django.shortcuts import render, redirect
from .models import Feed
from .forms import FeedForm
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'feeds_list.html', {"feeds": feeds})

@login_required
def single_feed(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'single_feed.html', {"feed": feed})


def create_feed(request):
    if(request.method == "POST"):
        form = FeedForm(request.POST)
        
        if form.is_valid():
            feed = form.save(commit=False) #pseudo save
            feed.published_date = date.today()
            form.save() # full save
            return redirect("feeds_list")
    else:
        # for GET request
        form = FeedForm()
        return render(request, "create_feed.html", {"form": form})
    
def edit_feed(request, id):
    feed = Feed.objects.get(id = id)
    
    if(request.method == "POST"):
        form = FeedForm(request.POST, instance=feed)
        
        if form.is_valid():
            feed = form.save(commit=False)
            feed.published_date = date.today()
            form.save()
            return redirect("feeds_list")
    else:
        form = FeedForm(instance=feed)
        return render(request, "edit_feed.html", {"form": form})

def delete_feed(request, id):
    
    feed = Feed.objects.get(id  = id)
    
    if(request.method == "POST"):
        feed.delete()
        return redirect("feeds_list")
    

