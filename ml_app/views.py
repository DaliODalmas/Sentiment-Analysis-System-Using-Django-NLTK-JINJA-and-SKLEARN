from django.shortcuts import render
import requests
import pickle
from . import preprocess

# Create your views here.
def predict(request):
    if request.method=='POST':
        message=request.POST.get('message',None)
        clean_message = preprocess.clean(message)

        with open('model.pickle', 'rb') as f:
            ml_model = pickle.load(f)
        
        result={'res':ml_model.classify(clean_message).upper()}
        
        return render(request,'ContactFrom/results.html',result)

    else:
        return render(request,'ContactFrom/index.html')