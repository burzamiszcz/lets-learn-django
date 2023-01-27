from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import CreateNewAd
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max

# Create your views here.

def index(request):
    adList = Ad.objects.all()

    return render(request, "main/home.html", {"userList":adList})

@login_required(login_url="/login")
def add_new_offer(request):
    form = CreateNewAd()
    if request.method == "POST":
        form = CreateNewAd(request.POST)

        if form.is_valid():
            print('udalo sie')
            newAd = form.save(commit=False)
            newAd.username = request.user
            newAd.save()
                # user = User.objects.get(id=id)
    return render(request, "main/add_new_offer.html", {"form":form})


def show_offer(request, adId):
    user = request.user
    adData = Ad.objects.get(id = adId)
    print(adData.username)
    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        receiver = User.objects.get(username=adData.username)
        Message.objects.create(sender=user, receiver=receiver, message_text=message_text, offer = adData)

    return render(request, "main/ad.html", {"id":adId, 'adData':adData})




@login_required
def conversations(request):
    user = request.user
    # Get all unique conversation partners
    partners = (Message.objects.filter(sender=user).values('receiver__username', 'offer_id').distinct()
                .union(
                    Message.objects.filter(receiver=user).values('sender__username', 'offer_id').distinct()
                ))

    last_messages = {}
    ad_titles = {}
    for partner in partners:
        uniqe = str(partner['receiver__username']) + str(partner['offer_id'])
        last_messages[uniqe] = Message.objects.filter(Q(sender=user, receiver__username=partner['receiver__username'], offer=partner['offer_id']) | Q(sender__username=partner['receiver__username'], receiver=user, offer=partner['offer_id'])).order_by('-created_at').first()
        last_messages[uniqe] = last_messages[uniqe].get_message()

        ad_titles[partner['offer_id']] = Ad.objects.filter(id=partner['offer_id']).first()
        ad_titles[partner['offer_id']] = ad_titles[partner['offer_id']].get_title()


    context = {'partners': partners, 'last_messages': last_messages, 'ad_titles': ad_titles}
    return render(request, 'main/conversations.html', context)

@login_required
def conversation(request, receiver_username, adId):
    user = request.user
    offer = Ad.objects.get(id=adId)
    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        receiver = User.objects.get(username=receiver_username)

        #TODO Trzeba zczytywać Oferte ze strony oferty - zmienić url z zmienna oferty

    
        Message.objects.create(sender=user, receiver=receiver, message_text=message_text, offer = offer)
    # messages = Message.objects.filter(sender=user, receiver__username=receiver_username) | Message.objects.filter(sender__username=receiver_username, receiver=user)
    messages = Message.objects.filter(Q(sender=user, receiver__username=receiver_username, offer=adId) | Q(sender__username=receiver_username, receiver=user, offer=adId))
    messages = messages.order_by('-created_at')
    context = {'messages': messages, 'receiver_username': receiver_username, 'offer': offer}
    
    print(messages)
    return render(request, 'main/conversation.html', context)

