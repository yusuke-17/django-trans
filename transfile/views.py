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
    result_file = ""
    file_name = ""

    if request.method == "POST":
        form = TransFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # ファイル取得
            file = models.FileUpload.objects.order_by("id").last()
            file_name = settings.BASE_DIR + file.uploadedFile.url
            root, ext = os.path.splitext(file_name)
            result_file = root + '_EN' + ext
            
            if file.uploadedFile.url and result_file:
                translator = deepl.Translator(settings.DEEPL_API_KEY)
                # 日本語に翻訳
                translator.translate_document_from_filepath(
                    file_name,
                    result_file,
                    source_lang='JA',
                    target_lang='EN-US'
                )
                # ファイルパスと名前取得
                dirname, basename = os.path.split(result_file)
    else:
        form = TransFileForm()
    temp = loader.get_template('transfile/index.html')
    context = {
        'trans_result': result_file
    }
    if result_file:
        return FileResponse(open(result_file, "rb"), as_attachment=True, filename=basename)
    return HttpResponse(temp.render(context, request))

# Create your views here.
