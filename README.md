# AI based Text Generation Web Application

This repository contains the production ready web application for artificial text generation using GPT2. Web application takes input from the user and displays the output to the user.

Note: Front-end is very basic created for only for testing purposes. As, this is just MVP for the demo purposes to the clients. 

Prerequistes: You should have docker and python 3.6 or above installed on your machine.
 
To keep the process simple I have created shell file which can develop entire application for the user.

***Note: This application can take input from user using a webform or you can run jupyter notebook to send the input. Current version of the code takes input from the POST requests send through jupyter notebook.***

1. Open the terminal and clone the repo to your machine.
```
git clone https://github.com/VAIBHAVPATEL97/Task2-fizzbuzz.git
```
2. Navigate to the repository folder and run the 'run_and_build_docker.sh' file using the following command:
```
sudo bash run_and_build_docker.sh 
```
3. If there are no errors in the last step you can run the following command to confirm flask and nginx containers are up and running.
```
docker-compose ps
```
Reason to select the GPT-2 model from hugging faces is solely based on my interest to explore the model. More details can be found in jupyter notebook in this repo.

Note: If there are any issues with the repository feel free to create good first issue I will be happy to solve. 

Cheers!! Keep learning and evolving..
