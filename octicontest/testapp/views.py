from django.shortcuts import render
from django.shortcuts import render
from octicons.templatetags.octicons import Octicon
from octicons.templatetags import OCTICON_DATA

def index(request):
    # import ipdb; ipdb.set_trace()
    Octicon.register('pen', '/home/srijan/Documents/svg_script/pen.svg')
    print(OCTICON_DATA.get('x')['path'])
    return render(request, 'index.html')
