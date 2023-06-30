# AI based Text Generation Web Application

This repository contains the production-ready prototype web application for artificial text generation using GPT2. Web application takes input from the user and displays the output to the user.

Note: Front-end is very basic and created only for testing purposes. As this is just MVP for the demo purposes to the clients. For demo purposes, the out-of-the-box GPT-2 model is used. It will be replaced by our trained domain-specific GPT-3 model (as discussed in the client meeting).

Prerequisites: You should have docker and python 3.6 or above installed on your machine.
 
To simplify the process, I have created a shell file that can develop an entire application for the user.

***Note: This application can take input from the user using a web form or you can run jupyter notebook to send the input. The current version of the code takes input from the POST requests sent through jupyter notebook.***

1. Open the terminal and clone the repo to your machine.
```
git clone https://github.com/VAIBHAVPATEL97/Task2-fizzbuzz.git
```
2. Navigate to the repository folder and run the 'run_and_build_docker.sh' file using the following command:
```
sudo bash run_and_build_docker.sh 
```
3. If there are no errors in the last step, you can run the following command to confirm flask and nginx containers are up and running.
```
docker-compose ps
```

Note: If there are any issues with the repository, feel free to create a good first issue I will be happy to solve. 

