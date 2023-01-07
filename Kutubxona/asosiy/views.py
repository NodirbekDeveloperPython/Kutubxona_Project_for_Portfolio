from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def sinashga(request):
    return HttpResponse("Salom Dunyo!")

def Bosh_sahifa(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect("/")

def register(request):
    if request.method == "POST":
        User.objects.create_user(
            username = request.POST.get("login"),
            password = request.POST.get("parol"),
        )
        return redirect("/")
    return render(request, 'register.html')

def loginView(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("login"),
                            password=request.POST.get("parol"))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/bosh_sahifa/")
    return render(request, 'loginView.html')

def logoutView(request):
    logout(request)
    return redirect("/")

def Mualliflar(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            forma = MuallifModelForm(request.POST)
            if forma.is_valid():
                forma.save()
            return redirect('/mualliflar/')
            # if request.POST.get("tirik") == "on":
            #     tirik = True
            # else:
            #     tirik = False
            # Muallif.objects.create(
            #     ism = request.POST.get("m_ism"),
            #     tirik = tirik,
            #     kitob_soni = request.POST.get("k_soni"),
            #     tugilgan_yil = request.POST.get("t_yil"),
            # )
            # return redirect('/mualliflar/')
        soz = request.GET.get('searching')
        if soz is None:
            M = Muallif.objects.all()
        else:
            M = Muallif.objects.filter(ism__contains=soz)
        data = {
            # Tirik mualliflarni chiqaring.
            # 'mualliflar': Muallif.objects.filter(tirik=True)

            # Kitobi eng ko’p 3 ta muallifni chiqaring.
            # 'mualliflar': Muallif.objects.order_by("-kitob_soni")[:3]


            # 13. Tug’ilgan yilidan kelib chiqib yoshi eng katta bo’lgan 3 ta muallifni chiqaruvchi view/html yozing.
            # 'mualliflar': Muallif.objects.order_by("tugilgan_yil")[:3]


            # 14. Kitob soni 10 tadan kichik bo’lgan mualliflarning hamma kitoblarini chiqaruvchi view/html yozing.
            # 'mualliflar': Muallif.objects.filter(kitob_soni__lt=10)


            # 4. Hamma mualliflarni chiqaruvchi sahifaga muallifni ismi bo’yicha qidirish imkoniyatini qo’shing.
            'mualliflar': M,
            'forma': MuallifModelForm()
        }
    else:
        return redirect("/")
    return render(request, 'mualliflar/mualliflar.html', data)

def muallif(request, pk):
    if request.user.is_authenticated:
        data = {
            "muallif": Muallif.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'mualliflar/muallif.html', data)

def Muallif_edit(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get("tirik") == "on":
                tirik = True
            else:
                tirik = False
            Muallif.objects.filter(id=pk).update(
                ism = request.POST.get("m_ism"),
                tirik = tirik,
                kitob_soni = request.POST.get("k_soni"),
                tugilgan_yil = request.POST.get("t_yil"),
            )
            return redirect('/mualliflar/')
        data = {
            'muallif':Muallif.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'mualliflar/muallif_edit.html',data)

def Muallif_ochir_tas(request,pk):
    if request.user.is_authenticated:
        data = {
            'muallif': Muallif.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'mualliflar/muallif_tas_ochir.html', data)

def muallif_ochir(request,pk):
    if request.user.is_authenticated:
        # 2. Biron muallifni o’chirib yuborish uchun view yozing.
        Muallif.objects.get(id=pk).delete()
    else:
        redirect("/")
    return redirect('/mualliflar/')



def Kitoblar(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            forma = MuallifModelForm(request.POST)
            if forma.is_valid():
                forma.save()
            return redirect('/kitoblar/')
            # Kitob.objects.create(
            # nom = request.POST.get("nom"),
            # sahifa = request.POST.get("sahifa"),
            # janr = request.POST.get("janr"),
            # muallif = Muallif.objects.get(id=request.POST.get("muallif"))
            # )
            # return redirect('/kitoblar/')
        soz = request.GET.get("q_soz")
        if soz is None:
            kitoblar = Kitob.objects.all()
        else:
            kitoblar = Kitob.objects.filter(nom__contains=soz)
        data = {
            # Sahifasi eng katta 3 ta kitobni chiqaring.
            # 'kitoblar': Kitob.objects.order_by("-sahifa")[:3]

            # 10. Tirik mualliflarning kitoblarini chiqaring.
            # 'kitoblar': Kitob.objects.filter(muallif__tirik=True)

            # 11. Hamma ‘badiiy’ kitoblarni chiqaring.
            'kitoblar': kitoblar,
            'mualliflar': Muallif.objects.all(),
            'forma': KitobModelForm()


            # "kitoblar": Kitob.objects.all()
        }
    else:
        return redirect("/")
    return render(request, 'kitoblar/kitoblar.html', data)

def kitob(request, pk):
    if request.user.is_authenticated:
        data = {
            "kitob": Kitob.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'kitoblar/kitob.html', data)

def Kitob_edit(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            Kitob.objects.filter(id=pk).update(
            nom = request.POST.get("nom"),
            sahifa = request.POST.get("sahifa"),
            janr = request.POST.get("janr"),
            muallif = Muallif.objects.get(id=request.POST.get("muallif"))
            )
            return redirect('/kitoblar/')
        data = {
            'kitob': Kitob.objects.get(id=pk),
            'mualliflar': Muallif.objects.all()
        }
    else:
        return redirect("/")
    return render(request, 'kitoblar/kitob_edit.html', data)

def Kitob_tas_ochir(request, pk):
    if request.user.is_authenticated:
        data = {
            'kitob': Kitob.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'kitoblar/kitob_tas_ochir.html', data)

def Kitob_ochir(request,pk):
    if request.user.is_authenticated:
        Kitob.objects.get(id=pk).delete()
    else:
        return redirect("/")
    return redirect('/kitoblar/')

def Recordlar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # forma = RecordForm(request.POST)
            # if forma.is_valid():
            #     forma.save()
            # return redirect('/recordlar/')
            if request.POST.get("qaytarilganmi") == "on":
                natija = True
            else:
                natija = False
            Record.objects.create(
                student = Student.objects.get(id=request.POST.get("talaba")),
                kitob = Kitob.objects.get(id=request.POST.get("kitob")),
                olingan_sana = request.POST.get("olingan_sana"),
                qaytardi = natija,
                qaytargan_sana = request.POST.get("qaytargan_sana"),
            )
        return redirect('/recordlar/')

        # 1Next lesson
        # 1. Hamma recordlarni chiqaruvchi sahifaga student ismi bo’yicha recordlarni qidirish imkoniyatini qo’shing.
        soz = request.GET.get('q_soz')
        if soz is None:
            recordlar = Record.objects.all()
        else:
            recordlar = Record.objects.filter(student__ism__contains=soz)

        data = {
            # 9. Recordlarni olingan sanasi bo’yicha eng oxirgi 3 tasini chiqaring.
            # 'recordlar': Record.objects.order_by("-olingan_sana")[:3]


            # 17. Bitiruvchi studentlarga tegishli hamma recordlarni chiqaruvchi html/view yozing.
            # 'recordlar': Record.objects.filter(student__bitiruvchi=True)

            # 1Next lesson Views
            # 1. Hamma recordlarni chiqaruvchi sahifaga student ismi bo’yicha recordlarni qidirish imkoniyatini qo’shing.
            # 'recordlar': recordlar

            'talabalar': Student.objects.all(),
            'kitoblar': Kitob.objects.all(),
            'recordlar': recordlar,
            # 'forma': RecordForm()
        }
    else:
        return redirect("/")
    return render(request, 'recordlar/recordlar.html', data)

def record(request, pk):
    if request.user.is_authenticated:
        data = {
            # 16. Tanlangan biron id’dagi recorddagi hamma ma’lumotlarni chiqaruvchi html/view yozing.
            'record': Record.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'recordlar/record.html', data)

def Record_edit(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get("qaytarilganmi") == "on":
                natija = True
            else:
                natija = False
            Record.objects.filter(id=pk).update(
                olingan_sana = request.POST.get("olingan_sana"),
                qaytardi = natija,
                qaytargan_sana = request.POST.get("qaytargan_sana"),
            )
            return redirect('/recordlar/')
        data = {
            "record": Record.objects.get(id=pk),
            "talabalar": Student.objects.all(),
            "kitoblar": Kitob.objects.all()
        }
    else:
        return redirect("/")
    return render(request, 'recordlar/record_edit.html',data)

def Record_tas_ochir(request, pk):
    if request.user.is_authenticated:
        data = {
            'record': Record.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'recordlar/record_tas_ochir.html',data)

def Record_ochir(request,pk):
    if request.user.is_authenticated:
        # 3. Biron recordni o’chirib yuborish uchun view yozing.
        Record.objects.get(id=pk).delete()
    else:
        return redirect("/")
    return redirect('/recordlar/')

def Talabalar(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            forma = TalabaForm(request.POST)
            if forma.is_valid():
                forma.save()
            return redirect('/talabalar/')
            # if request.POST.get("bitiruvchi") == "on":
            #     natija = True
            # else:
            #     natija = False
            # Student.objects.create(
            #     ism = request.POST.get("ism"),
            #     jins = request.POST.get("jins"),
            #     bitiruvchi = natija,
            #     kitob_soni = request.POST.get("k_soni"),
            # )
            # return redirect('/talabalar/')
        soz = request.GET.get("q_soz")
        if soz is None:
            talabalar = Student.objects.all()
        else:
            talabalar = Student.objects.filter(ism__contains=soz)
        data = {
            # 12. Ismida ‘a’ qatnashgan studentlarni chiqarish
            # 'talabalar': Student.objects.filter(ism__contains="a")


            # 15. Erkak studentlarni chiqaring.
            # 'talabalar': Student.objects.filter(jins="Erkak")


            'forma': TalabaForm(),
            'talabalar': talabalar
        }
    else:
        return redirect("/")
    return render(request, 'talabalar/talabalar.html', data)

def talaba(request, pk):
    if request.user.is_authenticated:
        data = {
            'talaba': Student.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'talabalar/talaba.html', data)

def Talaba_edit(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get("bitiruvchi") == "on":
                natija = True
            else:
                natija = False
            Student.objects.filter(id=pk).update(
                ism = request.POST.get("ism"),
                jins = request.POST.get("jins"),
                bitiruvchi = natija,
                kitob_soni = request.POST.get("k_soni"),
            )
            return redirect('/talabalar/')
        data = {
            "talaba": Student.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'talabalar/talaba_edit.html', data)

def Talaba_tas_ochir(request, pk):
    if request.user.is_authenticated:
        data = {
            "talaba": Student.objects.get(id=pk)
        }
    else:
        return redirect("/")
    return render(request, 'talabalar/talaba_tas_ochir.html', data)

def Talaba_ochir(request,pk):
    if request.user.is_authenticated:
        Student.objects.get(id=pk).delete()
    else:
        return redirect("/")
    return redirect("/talabalar/")