# Deployment-of-dockerised-flask-api-into-kubernetes
First create an api using flask

Then create a dockerfile and requirements.txt file

Then use docker build -t flask-app command  to build a dockerimage

Then to deploy this dockerized flask-api into the kubernetes we make a deployment.yaml file 

We are using minikube as local kubernetes cluster 

Then run the the command kubectl apply -f dployment.yaml command so that it creates the flask-test and serivce flask-test service

To check the status of the pods we use kubectl get pods

To run the this flask api which is deployed into kubernetes we use the command minikube services flask-test-service which provides the url 

Run this url on your browser to access the api
