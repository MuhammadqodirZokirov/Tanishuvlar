from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from chat.models import Message, UserProfile
from chat.serializers import MessageSerializer, UserSerializer


def index(request):
    if request.user.is_authenticated:
        return redirect('chats')
    if request.method == 'GET':
        return render(request, 'chat/index.html', {})
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('{"error": "User does not exist"}')
        return redirect('chats')


@csrf_exempt
def user_list(request, pk=None):
    if request.method == 'GET':
        if pk:
            users = User.objects.filter(id=pk)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.create_user(username=data['username'], password=data['password'])
            UserProfile.objects.create(user=user)
            return JsonResponse(data, status=201)
        except Exception:
            return JsonResponse({'error': "Something went wrong"}, status=400)


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('chats')
    return render(request, 'chat/register.html', {})


def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'chat/chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, "chat/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)})


def asosiy(request):
    context = {}
    data = UserProfile.objects.all()
    count = len(data)
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data1 = UserProfile.objects.get(user__id=request.user.id)
        context = {
            'usr': data1,
            'count': count,
        }
    return render(request, 'chat/index1.html', context)


def adminChat(request):
    context = {}
    usr = UserProfile.objects.filter(user__id=request.user.id)
    Admins = User.objects.filter(is_superuser=True)
    context = {
        'usr': usr,
        'categories': Admins,
    }
    return render(request, 'chat/lider.html', context)


def friend(request):
    context = {}
    data = UserProfile.objects.all()
    count = len(data)
    context = {
        'users': data,
        'count': count,
    }
    return render(request, 'chat/friend.html', context)


def albom(request):
    context = {}
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['usr'] = data
    return render(request, 'chat/albom.html', context)


def status(request):
    context = {}
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['usr'] = data
    return render(request, 'chat/status.html', context)


def oyin(request):
    context = {}
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data1 = UserProfile.objects.get(user__id=request.user.id)
        context = {
            'usr': data1,
        }
    return render(request, 'chat/oyinlar.html', context)


def extra(request):
    context = {}
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data1 = UserProfile.objects.get(user__id=request.user.id)
        context = {
            'usr': data1,
        }
    return render(request, 'chat/extra.html', context)


def kurs(request):
    import requests
    context = {}
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data1 = UserProfile.objects.get(user__id=request.user.id)
        context = {
            'usr': data1,
        }
    url = 'https://v6.exchangerate-api.com/v6/1cca2aaaa843438ba85f26c7/pair/EUR/UZS'
    response = requests.get(url)
    EURO = response.json()
    print(EURO['conversion_rate'])
    url = 'https://v6.exchangerate-api.com/v6/1cca2aaaa843438ba85f26c7/pair/USD/UZS'
    response = requests.get(url)
    USD = response.json()
    print(USD['conversion_rate'])
    url = 'https://v6.exchangerate-api.com/v6/1cca2aaaa843438ba85f26c7/pair/RUB/UZS'
    response = requests.get(url)
    RUB = response.json()
    print(RUB['conversion_rate'])
    context = {
        'EURO': EURO['conversion_rate'],
        'USD': USD['conversion_rate'],
        'RUB': RUB['conversion_rate'],
    }
    return render(request, 'chat/kursv.html', context)


def allfotoalbom(request):
    context = {}
    data = UserProfile.objects.all()
    context['data'] = data
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data1 = UserProfile.objects.get(user__id=request.user.id)
        context = {
            'usr': data1,
        }
    return render(request, 'chat/allfotoalbom.html', context)


def levelbuy(request):
    context = {}
    data = UserProfile.objects.filter(user__id=request.user.id)
    if len(data) > 0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['data'] = data
    if request.method == 'POST':
        reyting = request.POST['reytingplus']

        if int(reyting) <= data.reyting:
            data.reyting = data.reyting + int(reyting)
            data.pul -= int(reyting) * 100
            data.save()
            context['msg'] = 'Reyting Muvafaqiyatli qo\'shildi!!!'
            context['error'] = 'alert-success'
        else:
            context['msg'] = 'Pulingiz yetarli emas reyting qo\'shilmadi!!!'
            context['error'] = 'alert-danger'

    return render(request, 'chat/levelbuy.html', context)


def othersection(request):
    context = {}
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data1 = UserProfile.objects.get(user__id=request.user.id)
        context = {
            'usr': data1,
        }
    return render(request, 'chat/othersection.html', context)


def anketa(request):
    context = {}
    data = UserProfile.objects.filter(user__id=request.user.id)
    if len(data) > 0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['data'] = data
    return render(request, 'chat/anketa.html', context)


def settings(request):
    context = {}
    data = UserProfile.objects.filter(user__id=request.user.id)
    if len(data) > 0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['data'] = data
    return render(request, 'chat/settings.html', context)


def personalChange(request):
    context = {}
    data = UserProfile.objects.filter(user__id=request.user.id)
    if len(data) > 0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['data'] = data
    if request.method == 'POST':
        gender = request.POST['gender']
        first = request.POST['firstname']
        last = request.POST['lastname']
        age = request.POST['age']
        city = request.POST['city']
        phone = request.POST['phone']
        about = request.POST['about']
        data.gender = gender
        data.age = age
        data.first_name = first
        data.last_name = last
        data.city = city
        data.phone = phone
        data.about = about
        if 'pg_img' in request.FILES:
            data.profile_img = request.FILES['pg_img']
            if 'bg_img' in request.FILES:
                data.bg_img = request.FILES['bg_img']
                data.save()
        data.save()
        context = {
            'data': data,
        }
        context['msg'] = 'Shaxsiy Ma\'lumotlaringiz Muvafaqiyatli O\'zgartirildi !!!'
        context['error'] = 'alert-success'
    return render(request, 'chat/personnalinfChange.html', context)


def support(request):
    usr = UserProfile.objects.filter(user__id=request.user.id)
    if len(usr) > 0:
        data1 = UserProfile.objects.get(user__id=request.user.id)
        context = {
            'usr': data1,
        }
    return render(request, 'chat/hisob.html', context)


def change_password(request):
    context = {}
    ch = UserProfile.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['data'] = data
    if request.method == 'POST':
        current = request.POST['current_password']
        new_password = request.POST['new_password']
        user = User.objects.get(id=request.user.id)
        username = user.username
        check = user.check_password(current)

        if check == True:
            context['msg'] = 'Password changed successfully!!!'
            context['error'] = 'alert-success'
            user.set_password(new_password)
            user.save()
            user = User.objects.get(username=username)
            login(request, user)
        else:
            context['msg'] = 'Incorrect your password'
            context['error'] = 'alert-danger'

    return render(request, 'chat/passwordchange.html', context)


def change_username(request):
    context = {}
    ch = UserProfile.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['data'] = data
    if request.method == 'POST':
        current = request.POST['current_username']
        new_username = request.POST['new_username']
        user = User.objects.get(id=request.user.id)

        if user.username == current:
            context['msg'] = 'Username changed successfully!!!'
            context['error'] = 'alert-success'
            user.username = new_username
            user.save()
            user = User.objects.get(username=new_username)
            login(request, user)
        else:
            context['msg'] = 'Incorrect your username'
            context['error'] = 'alert-danger'
    return render(request, 'chat/loginchange.html', context)

def yangiyil(request):
    return render(request, 'chat/index2.html')
def obxavo(request):
    return render(request, 'chat/index3.html')
def youtubedownload(request):
    context = {}
    if request.method == 'POST':
        link = request.POST['youtube']
        from pytube import YouTube
        video = YouTube(f'{link}').streams.get_highest_resolution().url
        context['video'] = video
    return render(request, 'chat/YoutubeDownloader.html', context)

def tiktokdownload(request):
    context = {}
    if request.method == 'POST':
        link = request.POST['tiktok']
        import requests

        url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

        querystring = {"url": link}

        headers = {"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com",
                   "X-RapidAPI-Key": "ac4cc9fd65mshef9ecd072aeb911p1cba1djsn75e88102fd2d"}

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.json()
        natija = {"video": result['video'][0], "music": result['music'][0]}
        context['video'] = natija['video']
    return render(request, 'chat/tiktokdownload.html', context)