from django.shortcuts import render
from .forms import ResumeUploadForm
from .utils import extract_text_from_pdf
from .services.ai_service import analyze_resume_with_ollama


def upload_resume(request):
    extracted_text = None
    ai_response = None

    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            extracted_text = extract_text_from_pdf(resume.file)

            print(extracted_text)
            ai_response = analyze_resume_with_ollama(extracted_text)

    else:
        form = ResumeUploadForm()

    return render(request, "upload.html", {
        "form": form,
        "text": extracted_text,
        "ai_response": ai_response
    })
