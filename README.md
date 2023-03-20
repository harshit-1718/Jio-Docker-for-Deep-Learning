# PS1

To run the flask APP locally, download all folders except "docerised_rabbitmq"

You will need to run three different terminals together to run the APP with rabbitmq. Run the flask API first using flask run command
Run the requirements.txt file to install all dependencies(using pip install -r requirements.txt)
Then run the consumer_ans.py and consumer_question.py in seperate containers.
Then make a request at the API of the form /create-job/"QUESTION TEXT"

You can see your question Text at the consumer_question.py terminal. And answer at consumer_ans.py terminal...

To Run the dockerised version. Download that folder individually and run the requirements file similarly. 
Then run the docker-compose up command
to build all the docker containers. You can open the API from the server container and management console from the docker container of rabbitmq.
After that you will see the final output at the consumer container terminal.

Note due to so many dependencies there might be issue while running requirements.txt file. To debug that 
open the server and worker services in bash mode (tail flag command) and then use pip freeze to see the dependencies install
After that you can install any dependency from there only directly inside the container.
Also you can run the app.py file directly from there.

To run the flask API on Kubernetes, see the Flask_Kubernetes folder.

