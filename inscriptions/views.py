from django.shortcuts import render, redirect
from .forms import CandidatForm
from django.shortcuts import get_object_or_404
from .models import Candidat
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
import base64
from django.conf import settings
def inscription_view(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save()
            return redirect('confirmation', pk=candidat.pk)
    else:
        form = CandidatForm()
    return render(request, 'inscriptions/inscription_form.html', {'form': form})

def confirmation_view(request, pk):
    candidat = get_object_or_404(Candidat, pk=pk)
    return render(request, 'inscriptions/confirmation.html', {'candidat': candidat})


def generer_recu_pdf(request, pk):
    candidat = get_object_or_404(Candidat, pk=pk)
    template_path = 'inscriptions/reçu_pdf.html'
    context = {'candidat': candidat}

    # Convertir la photo en base64 pour l'inclure dans le PDF
    if candidat.photo:
        photo_path = os.path.join(settings.MEDIA_ROOT, candidat.photo.name)
        try:
            with open(photo_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            context['photo_base64'] = f"data:image/jpeg;base64,{encoded_string}"
        except Exception as e:
            context['photo_base64'] = None
    else:
        context['photo_base64'] = None

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="recu_{candidat.nom}_{candidat.prenoms}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    # Génération du PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF', status=500)
    return response
