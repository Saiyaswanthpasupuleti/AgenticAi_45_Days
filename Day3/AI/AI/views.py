from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ollama import Client
import json

@csrf_exempt
def chat(request):
    client = Client(
        host="http://localhost:11434"
    )
    if request.method == 'POST':
        bodyMessage = json.loads(request.body)
        message_content = bodyMessage.get('message') 
        stream = client.chat(
            model="gemma3:270m",
            messages=[{"role": "user", "content": message_content}]
        )
        return HttpResponse(stream.message.content)