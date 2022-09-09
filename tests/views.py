from django.contrib.messages.storage.session import SessionStorage
from django.shortcuts import render, redirect
from .models import Test, Answers, Predmeti
from django.http.response import JsonResponse, HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import openpyxl

from openpyxl.utils.cell import coordinate_from_string
import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing

def tochnost(idd):
    t_ = pd.read_excel("date.xlsx")
    id_ = idd
    df = pd.DataFrame(t_)
    df1 = df.loc[df['ID'] == id_]
    DF_ = df1.drop_duplicates(keep='first', subset='Date')
    horizon_ = 1
    z_1 = DF_.drop(columns=[1, 'Min', 'ID'], axis=1)
    train_lenght = len(z_1) - horizon_
    train = z_1.drop(z_1.index[train_lenght])
    test = z_1['Average'].iloc[-1]
    d_train = train['Date'].tolist()
    ptrain = d_train[-1] + horizon_
    d_1train = np.append(d_train, ptrain)

    fit1_train = ExponentialSmoothing(train['Average'], seasonal_periods=None,
                                      trend='add', seasonal=None, damped_trend=True).fit()
    fitted_train = fit1_train.predict(0, len(train) + horizon_ - 1)

    Df_train = np.round(fitted_train, 2)
    df_ftrain = pd.DataFrame(Df_train)
    df_ftrain.columns = ['Average']
    df_ftrain.insert(0, "Date", d_1train, False)
    y_pred = df_ftrain['Average'].iloc[-1]
    y_true = z_1['Average'].iloc[-1]

    f = (y_true / y_pred) * 100  # отношение факта к прогнозу ВАР1
    o = y_true - y_pred  # ошибка прогнозной модели
    ma = o ** 2 / y_pred ** 2
    #t1 = (1 - ma) * 100  # точность прогноза ВАР2
    MAPE = np.mean(np.abs(y_pred - test) / test) * 100
    t1 = 100 - MAPE

    return t1


def stat(kod):
    t = pd.read_excel("date.xlsx")
    id_ = str(kod).strip().replace('.',' ')
    toch = tochnost(id_)
    horizon_ = 1

    df = pd.DataFrame(t)
    df1 = df.loc[df['ID'] == id_]
    DF = df1.drop_duplicates(keep='first', subset='Date')
    DF1 = DF.drop(columns=[1, 'Min', 'ID'], axis=1)

    d_ = DF1['Date'].tolist()
    p = d_[-1]+horizon_
    d_1 = np.append(d_, p)

    z_1 = DF1
    fit1 = ExponentialSmoothing(z_1['Average'], trend='add', damped_trend=True,
                                seasonal=None, seasonal_periods=None).fit()
    fitted_ = fit1.predict(0, len(z_1) + horizon_ - 1)

    Df = np.round(fitted_, 2)
    df_f = pd.DataFrame(Df)

    df_f.columns = ['Average']
    df_f.insert(0, "Date", d_1, False)

    last = df_f['Average'].iloc[-1]
    return last, toch


def home(request):

    request.session.set_expiry(500)
    session = request.session.keys()
    return render(request, 'tests/home.html', {'Tests': Test.objects.all(), 'ses':session})


def test(request, pk):
    test = Test.objects.get(pk=pk)
    request.session[test.title] = True
    check = ''
    try:
        check = request.session['checkpoint']
    except:
        check = ''
    print(check)

    if check != '':
        if (check == 'ege'):
            return redirect("ege")
        else:
            first_question = test.questions.get(pk=int(check))
    else:
        first_question = test.questions.first()


    return render(request, 'tests/test.html', {'Test': test, 'Question': first_question, 'Last': test.questions.last().id})


def next_question (request, pk):
    id = request.GET.get('id')
    lastt = str(request.GET.get('last'))
    global datas
    global question
    answer = request.GET.get('answer')
    test = Test.objects.get(pk=pk)
    result = str(request.GET.get('res'))
    if (str(result) != 'None'):

        print(lastt)
        print(result)
        return render(request, 'tests/result.html',{'res': result})
    else:
        if (id == str(1)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=1).values('text', 'id')[:1]
        if (id == str(1)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=7).values('text', 'id')[:1]

        if (id == str(2)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=3).values('text', 'id')[:1]
        if (id == str(2)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=9).values('text', 'id')[:1]

        if (id == str(3)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=4).values('text', 'id')[:1]
        if (id == str(3)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=6).values('text', 'id')[:1]

        if (id == str(4)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=2).values('text', 'id')[:1]
        if (id == str(4)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=9).values('text', 'id')[:1]

        if (id == str(5)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=5).values('text', 'id')[:1]
        if (id == str(5)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=6).values('text', 'id')[:1]

        # if (id == str(6)) and (answer == str(1)):
        #     question = test.questions.filter(pk__gt=3).values('text', 'id')[:1] #Последний
        if (id == str(6)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=10).values('text', 'id')[:1]

        # if (id == str(7)) and (answer == str(1)):
        #     question = test.questions.filter(pk__gt=3).values('text', 'id')[:1] #Последний
        if (id == str(7)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=11).values('text', 'id')[:1]

        if (id == str(8)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=8).values('text', 'id')[:1]
        if (id == str(8)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=12).values('text', 'id')[:1]

        if (id == str(9)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=9).values('text', 'id')[:1]
        if (id == str(9)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=14).values('text', 'id')[:1]

        if (id == str(10)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=6).values('text', 'id')[:1]
        if (id == str(10)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=16).values('text', 'id')[:1]

        # if (id == str(11)) and (answer == str(1)):
        #     question = test.questions.filter(pk__gt=3).values('text', 'id')[:1] #Последний
        if (id == str(11)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=11).values('text', 'id')[:1]

        if (id == str(12)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=10).values('text', 'id')[:1]
        if (id == str(12)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=20).values('text', 'id')[:1]

        if (id == str(13)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=14).values('text', 'id')[:1]
        if (id == str(13)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=13).values('text', 'id')[:1]

        if (id == str(14)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=15).values('text', 'id')[:1]
        if (id == str(14)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=21).values('text', 'id')[:1]

        if (id == str(15)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=16).values('text', 'id')[:1]
        if (id == str(15)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=15).values('text', 'id')[:1]

        if (id == str(16)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=17).values('text', 'id')[:1]
        if (id == str(16)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=21).values('text', 'id')[:1]

        if (id == str(17)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=18).values('text', 'id')[:1]
        if (id == str(17)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=17).values('text', 'id')[:1]

        if (id == str(18)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=19).values('text', 'id')[:1]
        if (id == str(18)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=22).values('text', 'id')[:1]

        if (id == str(19)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=20).values('text', 'id')[:1]
        if (id == str(19)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=19).values('text', 'id')[:1]

        if (id == str(20)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=20).values('text', 'id')[:1]
        if (id == str(20)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=23).values('text', 'id')[:1]

        # if (id == str(21)) and (answer == str(1)):
        #     question = test.questions.filter(pk__gt=3).values('text', 'id')[:1] #Последний
        if (id == str(21)) and (answer == str(0)):
            question = test.questions.filter(pk__gt=24).values('text', 'id')[:1]

        if (id == str(22)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=22).values('text', 'id')[:1]
        # if (id == str(22)) and (answer == str(0)):
        #     question = test.questions.filter(pk__gt=11).values('text', 'id')[:1] #Последний

        if (id == str(23)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=23).values('text', 'id')[:1]
        # if (id == str(23)) and (answer == str(0)):
        #     question = test.questions.filter(pk__gt=11).values('text', 'id')[:1] #Последний

        if (id == str(24)) and (answer == str(1)):
            question = test.questions.filter(pk__gt=24).values('text', 'id')[:1]
        # if (id == str(24)) and (answer == str(0)):
        #     question = test.questions.filter(pk__gt=11).values('text', 'id')[:1]  # Последний

        # if (id == str(25)) and (answer == str(1)):
        #     question = test.questions.filter(pk__gt=23).values('text', 'id')[:1] # Последний
        # if (id == str(25)) and (answer == str(0)):
        #     question = test.questions.filter(pk__gt=11).values('text', 'id')[:1]  # Последний
        for i in question:
            datas = {
                'text': i['text'],
                'id': i['id']
            }
            request.session['checkpoint'] = i['id']
        answer = Answers(question=test.questions.get(pk=id), answer=answer)
        answer.save()
        print(request.session['checkpoint'])
    return JsonResponse({'data': datas})


def ege (request):
    print(request.session.get('Тест 1'))
    print(request.session.get('human'))
    return render(request, 'tests/ege.html', {'Predmeti': Predmeti.objects.all()})

@csrf_exempt
def info (request):
    predmets = request.POST.getlist('datas[]')
    type_L = request.session['human']
    t = pd.read_excel("1.xlsx")
    df = pd.DataFrame(t)
    df1 = df.loc[df['Тип личности'] == type_L]
    _p = []
    for i in range(0, len(predmets)):
        _p.append(predmets[i].rsplit(' ', 1))
    arr_p = []
    for i in range(0, len(_p)):
        arr_p.append(_p[i][0])
    del_ = []
    for i in df1.columns.tolist():
        if i not in arr_p:
            del_.append(i)
    DF = df1.drop(columns=del_, axis=1).dropna()
    sort = sorted(_p, key=lambda _p: int(_p[1]), reverse=True)
    sredniy = 0
    for i in sort:
        sredniy+=int(i[1])
    sredniy = sredniy / len(sort)
    ind = []
    for i in sort:
        if i[0] in DF.columns.tolist():
            for j in range(0, DF.shape[0]):
                if DF[i[0]].tolist()[j] == 1:
                    ind.append(DF[i[0]].index.tolist()[j])
        if len(ind) != 0:
            break
    napr =[]
    for i in range(0, df1.shape[0]):
        for j in ind:
            p = df1.loc[j]
            srbal = stat(p[13])
            print(srbal)
            napinfo = {'Направление': p[14], 'Профессии': p[1], 'Институт': p[15], 'Профильный предмет': sort[0][0],
                       'Тип личности': p[0], 'Вероятность балла': srbal[0], 'Тп': round(srbal[1],1), 'Сб': round(sredniy,1)}
            napr.append(napinfo)
        break
    geg = sorted(napr, key=lambda x: x['Вероятность балла'])
    return JsonResponse ({'data': geg})

@csrf_exempt
def result (request):
    res = request.POST.get('res')
    request.session['human'] = res
    request.session['checkpoint'] = 'ege'
    return HttpResponse('{"Status":"OK"}', status=200)

