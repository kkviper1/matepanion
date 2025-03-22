from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
import json
from .utils.llm import chat
from .utils.tts import speak

import re

def remove_think_tags(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "POST":
        incoming_msg = request.POST.get("Body", "").strip().lower()
        response = MessagingResponse()
        
        txt_reply = chat(incoming_msg)
        txt_reply = remove_think_tags(txt_reply)
        
        response.message(txt_reply)
        # speak(txt_reply)
        
        # runclient(txt_reply)
        

        return HttpResponse(str(response))
    return HttpResponse("Only POST requests are allowed", status=405)
