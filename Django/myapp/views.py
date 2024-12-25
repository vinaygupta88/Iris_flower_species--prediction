from django.shortcuts import render
import os
import pickle
# Create your views here.
def index(request):
    if request.method=='POST':
        sl=float(request.POST['sl'])
        sw=float(request.POST['sw'])
        pl=float(request.POST['pl'])
        pw=float(request.POST['pw'])
        path=os.path.dirname(__file__)
        model=pickle.load(open(os.path.join(path,'decision.pkl'),'rb'))
        res=model.predict([[sl,sw,pl,pl]])[0]
        return render(request,"index.html",{"res":res})
    return render(request,"index.html")