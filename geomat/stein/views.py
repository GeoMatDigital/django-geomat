from django.views.generic.list import ListView

from geomat.stein.models import Handpiece, Photograph

class GalleryListView(ListView):
    model = Photograph
    template_name = 'pages/preview.html'
