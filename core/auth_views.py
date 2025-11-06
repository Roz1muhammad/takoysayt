from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout


from core.auth_models import User


def register(request):
    ctx={}
    if request.POST:
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        pass_conf = request.POST.get("pass_conf")


        if None in [username,password,phone,pass_conf]:
            ctx["error"]="Poyalalarni toldring"
            return render(request, "register.html",ctx)


        user = User.objects.filter(username=username)
        if user :
            ctx["error"] = "Poyalalarni toldring"
            return render(request, "register.html", ctx)


        if password != pass_conf:
            ctx["error"] = "Poyalalarni toldring"
            return render(request, "register.html", ctx)

        User.objects.create_superuser(
            username=username,
            phone=phone,
            password=password
        )
        ctx['sucsses']= "succses"
        return render(request, "index.html", ctx)





    return render(request, "register.html",ctx)

def sgin_out(request):

    ctx={}
    name = request.POST.get("username")
    password = request.POST.get("password")
    if None in [name,password]:
        ctx["erorr"]="hamama polya tolishi shart"
        return render(request, "index.html",ctx)
    user = User.objects.filter(name=name).first()
    if not user:
        ctx["error"]="parol yo kida username hato"
        return render(request, "index.html",ctx)
    if not user.chesk.password("password"):
        ctx["error"]= "parol yo kida username hato"
        return render(request, "index.html", ctx)

    login(request, user)




    return render(request, "index.html",ctx )




