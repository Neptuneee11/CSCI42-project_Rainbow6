from django import forms

class bicycleForm(forms.Form):
    STATES = {
        "AV":"available",
        "IU":"in_use",
        "MAIN":"maintenance",
    }
    
    state = forms.CharField()
    STATIONS = {
        "BEL":"Bellarmine",
        "MACCI":"Matteo Ricci",
        "LEO":"Leong",
        "CTC":"CTC",
        "SEM":"Seminary",
    }
    location = forms.CharField()

