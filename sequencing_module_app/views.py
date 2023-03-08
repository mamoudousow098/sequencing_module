from django.shortcuts import render
from django.shortcuts import redirect 
from pathlib import Path
import requests
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
env.read_env(os.path.join(BASE_DIR, '.env'))
BASE_URL = env('BASE_URL')


# Create your views here.
def home_view(request, *args, **kwargs):
    
    response = requests.get(BASE_URL + 'api/token', headers= request.headers)
    print(response.json())

    if response.status_code == 200 :
        user = response.json()['data']
        return render(request, 'home.html', { 'user': user})
    else : 
        return redirect('/')



def login_view(request, *args, **kwargs):
    # response = requests.get(BASE_URL + 'api/token', headers= request.headers)
    # print(response.json())
    # if response.status_code == 200 :
    #     return redirect('/home')
    return render(request, 'login.html')



def test_view(request, *args, **kwargs):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    print(users)
    return render(request, 'test.html', { 'users': users})