# question-answering-system
It is a question-answering application that interacts with the Improvado website using Django and Chat GPT.
Integrating Chat GPT into a question-answering system opens up possibilities for natural language interactions, enabling users to obtain informative and accurate responses. By leveraging the capabilities of Chat GPT, developers can create intuitive and engaging applications that provide valuable assistance and support to users.

For the correct execution of the application in a local environment, the following steps should be followed:
1. The application was developed with the following dependencies:

            Django==4.2.1
            openai==0.27.6
            Python 3.10.6

2. This application interacts with the **OPEN AI API** for the question and answer system.  It is necessary to create an account in OPEN AI to obtain an API KEY and consume the **CHAT GPT** service.
    This API Key should be configured in the **settings.py** file located in the following repository path:

            questionAnsweringSys/questionAnsweringSys/settings.py

    The file **settings.py** contains the **API_KEY_OPEN_AI** variable. The value of this variable should be replaced with the API Key generated from OPEN AI. For more information about the OPEN AI API, you can visit this link:


            https://platform.openai.com/docs/api-reference/introduction


3. To start the server for this application, execute the **manage.py** file located in the following path:

            questionAnsweringSys/manage.py

    And run the following command to execute the manage.py file

            python3 manage.py runserver

4. The server is locally running on the http://127.0.0.1:8000 socket, and the following image indicates the homepage.
 
![Alt Text](images/homePage.png)

5. The following image shows an example of a response generated by Chat GPT. 

![Alt Text](images/responsePage.png)

