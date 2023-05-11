import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Answer
from django.utils import timezone
from django.shortcuts import render
from django.conf import settings


@csrf_exempt
def index(request):
    # This function loads the form for the user to enter the question.
    return render(request,"qanswering/index.html")


@csrf_exempt
def qanswering_view(request):
    # This function allows interacting the user's question with OPEN AI Chat GPT.
    if request.method == 'POST':
        # Assuming the user input is passed as a form parameter named 'questionUser'
        user_input = request.POST.get('questionUser')  

        # Send user input to OpenAI API for response generation
        openai.api_key = settings.API_KEY_OPEN_AI
        response = openai.Completion.create(
            engine='text-davinci-003',  # Specify the desired OpenAI engine
            prompt=user_input + ". Please consider the information at improvado.io",
            max_tokens=250,  # Adjust the desired response length
            n=1,
            stop=None,
            temperature=0.7
        )

        generated_response = response.choices[0].text.strip()

        # Save the question asked for the user and its answer
        user_question = Question(body_question = user_input, 
                                registration_date = timezone.now())
        user_question.save()
        user_question.answer_set.create(body_answer = generated_response,
                                       registration_date = timezone.now())

        # Return the generated response as a new page
        return render(request,
                      "qanswering/answeringResults.html",
                      {"answer_AI":generated_response,
                       "user_question":user_input})

    # Return an error if the request method is not POST
    return JsonResponse({'error': 'Invalid request method'})