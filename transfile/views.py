import deepl
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from . import models
from .forms import TransFileForm
from django.http import FileResponse

def index(request):
    file_name = ""
    result_file = ""
    trans_result = ""

    if request.method == "POST":
        # form = TransFileForm(request.POST)
        uploadedFile = request.FILES["uploadedFile"]
        document = models.FileUpload(
            uploadedFile = uploadedFile
        )
        document.save()

        # ファイル取得
        # file = models.FileUpload.objects.order_by("id").last()
        # file_name = file.uploadedFile.url
        # root, ext = os.path.splitext(file_name)
        # result_file = root + '_EN' + ext
        
        # translator = deepl.Translator(settings.DEEPL_API_KEY)
        # # 日本語に翻訳
        # trans_result = translator.translate_document_from_filepath(
        #     file_name,
        #     result_file,
        #     source_lang='JA',
        #     target_lang='EN-US'
        # )

        # if form.is_valid():
        #     translator = deepl.Translator(settings.DEEPL_API_KEY)
        #     # 翻訳文を取得
        #     sentence = form.cleaned_data['sentence']
        #     # 日本語に翻訳
        #     trans_result = translator.translate_text(sentence, source_lang='JA', target_lang='EN-US')
    # else:
    #     form = TransFileForm()
    temp = loader.get_template('transfile/index.html')
    context = {
        'trans_result': trans_result
    }
    # context = {
    #     'form': form,
    #     'trans_result': trans_result
    # }
    return HttpResponse(temp.render(context, request))

# Create your views here.
