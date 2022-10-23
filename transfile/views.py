from django.http import HttpResponse
from django.template import loader
from django.conf import settings

from .forms import TransFileForm
import deepl

def index(request):
    trans_result = ""

    if request.method == "POST":
        form = TransFileForm(request.POST)
        if form.is_valid():
            translator = deepl.Translator(settings.DEEPL_API_KEY)
            # 翻訳文を取得
            sentence = form.cleaned_data['sentence']
            # 日本語に翻訳
            trans_result = translator.translate_text(sentence, source_lang='JA', target_lang='EN-US')
    else:
        form = TransFileForm()
    temp = loader.get_template('transfile/index.html')
    context = {
        'form': form,
        'trans_result': trans_result
    }
    return HttpResponse(temp.render(context, request))

# Create your views here.
