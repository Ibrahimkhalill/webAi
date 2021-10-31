from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as Login_process ,logout,authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='login')
def Home(request):
    return render(request, 'webAi/home.html')


@login_required(login_url='login')
def submit(request):
    if request.method == 'GET':
        pass
    else:
        input1 = request.POST.get('input1')
        input1 = float(input1)
        input1 = round(input1, 2)
        input2 = request.POST.get('input2')
        input2 = float(input2)
        input2 = round(input1, 2)
        input3 = request.POST.get('input3')
        input3 = float(input3)
        input3 = round(input1, 2)
        input4 = request.POST.get('input4')
        input4 = float(input4)
        input4 = round(input1, 2)
        input5 = request.POST.get('input5')
        input5 = float(input5)
        input5 = round(input1, 2)
        input6 = request.POST.get('input6')
        input6 = float(input6)
        input6 = round(input1, 2)
        input7 = request.POST.get('input7')
        input7 = float(input7)
        input7 = round(input1, 2)
        input8 = request.POST.get('input8')
        input8 = float(input8)
        input8 = round(input1, 2)
        input9 = request.POST.get('input9')
        input9 = float(input9)
        input9 = round(input1, 2)
        input10 = request.POST.get('input10')
        input10 = float(input10)
        input10 = round(input1, 2)
        input11 = request.POST.get('input11')
        input11 = float(input11)
        input11 = round(input1, 2)
        input12 = request.POST.get('input12')
        input12 = float(input12)
        input1 = round(input1, 2)
        input13 = request.POST.get('input13')
        input13 = float(input13)
        input13 = round(input1, 2)
        input14 = request.POST.get('input14')
        input14 = float(input14)
        input14 = round(input1, 2)
        input15 = request.POST.get('input15')
        input15 = float(input5)
        input15 = round(input1, 2)
        input16 = request.POST.get('input16')
        input16 = float(input16)
        input16 = round(input1, 2)
        input17 = request.POST.get('input17')
        input17 = float(input17)
        input17 = round(input1, 2)
        input18 = request.POST.get('input18')
        input18 = float(input18)
        input18 = round(input1, 2)


        input19 = request.POST.get('input19')
        input19 = int(input19)
        input20 = request.POST.get('input20')
        input20 = int(input20)

    # Call Your API or function that will produce graph value using the inputs
    val = .3

    return render(request, 'webAi/new_page.html', {'val': val})

# https://jsfiddle.net/BlackLabel/x9vo0tr6/
def Login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            Login_process(request, user)
            return redirect('/')
        else:
             messages.info(request, 'Username OR password is incorrect')
    
    return render(request, 'webAi/login.html')


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username=request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if str(pass1) == str(pass2):
            user_object = User(first_name=fname, last_name=lname, email=email,username=username)
            user_object.set_password(pass1)
            user_object.save()

            return redirect('login')
        else:
            messages.error(request, 'Both Passwords did not match!')
            return render(request, 'webAi/register.html')

        
    return render(request, 'webAi/register.html')

def logoutUser(request):
    logout(request)
    return redirect('/')