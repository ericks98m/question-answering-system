import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

openai.api_key = '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'


def index(request):
    return render(request,"qanswering/index.html")


@csrf_exempt
def qanswering_view(request):
    if request.method == 'POST':
        # Assuming the user input is passed as a form parameter named 'input'
        user_input = request.POST.get('questionUser')  

        # Send user input to OpenAI API for response generation
        response = openai.Completion.create(
            engine='text-davinci-003',  # Specify the desired OpenAI engine
            prompt=user_input,
            max_tokens=250,  # Adjust the desired response length
            n=1,
            stop=None,
            temperature=0.7
        )

        generated_response = response.choices[0].text.strip()

        # Return the generated response as JSON
        return JsonResponse({'response': generated_response})

    # Return an error if the request method is not POST
    return JsonResponse({'error': 'Invalid request method'})