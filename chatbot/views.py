import ollama
from django.http import JsonResponse
from django.shortcuts import render

def generate_ollama_response(message):
    response = ollama.chat(
        model='phi',   
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response['message']['content'].strip()

def chat_page(request):
    return render(request, 'chatbot/chat.html')

def get_response(request):
    user_message = request.GET.get('message', '')
    if not user_message:
        return JsonResponse({'response': "Please enter a message."})

    try:
        bot_message = generate_ollama_response(user_message)
        return JsonResponse({'response': bot_message})
    except Exception as e:
        return JsonResponse({'response': f"Error: {str(e)}"})
