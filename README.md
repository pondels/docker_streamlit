# First Things First
## Open up Docker Desktop

# INSTRUCTIONS PART 1

## Step 1: Run this line of code

```docker pull ajaverett0/rps_game```

## Step 2: Run this line of code

```docker run -p 8501:8501 ajaverett0/rps_game```

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.   

# INSTRUCTIONS PART 2

## Prerequisites:

 - Make sure you open this folder in VS Code and are inspecting this markdown file in a pretty format.

 - Make sure yout working directory is this folder. 

## Step 1: Create a Docker account

Go to the following website and create an account with github if you haven't already.

[Click Me to Make a Docker Account](https://hub.docker.com/)


## Step 2: Create a Docker Repository

Once you are have created an account, go to the [repositories section](https://hub.docker.com/repositories/) and click the "Create repository" button and name it whatever you want

![](./images/create_repo.png)

- Once you do that, you will get a docker repository similar to the one you see above, where it's your docker <your username>, followed by the name of the repository.

(For example, if your <your username> was brighamyoung and your repository is called discourses, your repository path would be called, "*brighamyoung/discourses*")

## Step 3: Building the docker file

(When you are bulding your docker file, make sure you are logged in to your docker account on the docker desktop application on your computer)

-  Now we have to build the docker file to port it to our brand new repository.
-  We do this by using our Dockerfile, which you can browse
- ##### Be sure to replace the <your username>/<your repository name> with the appropriate information 

```docker build -t <your username>/<your repository name> -f ./Dockerfile .```

## Step 4: Push to your streamlet-docker application
```docker push <your username>/<your repository name>```

## Step 5: Pull the docker file
```docker pull <your username>/<your repository name>```

## Step 6: Start the instance
```docker run -p 8501:8501 <your username>/<your repository name>```

## Step 7: Launch the server under your localhost
http://localhost:8501/

---

For the most part, if you see something along the line of "select a repository" most times out of 10, it's the top one, but just check in your docker desktop that it's your image that you're working on before you do that.

# INSTRUCTIONS PART 3

When working with Docker and developing applications, the purpose of rebuilding the Docker image or using volumes/bind mounts is to ensure that the changes you make to your code or configuration files are reflected in the running container or in the final image. 

 ## Rebuilding the Docker image:

 - Docker images are like blueprints or templates for creating containers. They contain all the necessary dependencies, configurations, and code to run your application.
 - If you make changes to the Dockerfile or any files that are part of the image (e.g., dependencies), you need to rebuild the image to incorporate those changes.
 - Rebuilding the image ensures that when someone pulls your image or runs a container from it, they get the latest version with the updates you made.

 ## Using volumes or bind mounts:

 - Volumes and bind mounts provide a way to share files between your local machine and the running container.
 - With volumes, you create a separate volume that can be mounted to a specific directory inside the container. Any changes made to the files in the volume are immediately visible both inside the container and on your local machine.
 - Similarly, with bind mounts, you can directly mount a directory from your local machine into the container, and any changes made to the files in that directory are reflected in real-time.
 - Using volumes or bind mounts allows you to develop code locally on your machine using your favorite tools (like VSCode), while still being able to run and test the code inside the container with all the required dependencies.

The purpose of these approaches is to enable efficient development and deployment workflows. By rebuilding the Docker image or using volumes/bind mounts, you can make changes to your code or configuration files without needing to start the development environment from scratch or manually copy files into the container.

This flexibility allows you to iterate on your application quickly, test changes in a controlled environment, collaborate with others, and deploy updated versions of your application without disrupting the entire deployment process.

---
.
.
.


**The instructions below will initialize a volume (so we don't have to constantly rebuild the image for each modification). Our local path will act as the volume. Meaning, any changes that occur locally will sync up automatically with Docker desktop.**


## Step 8: Get required dependency
Install VSCode extension "Dev Containers"

## Step 9: Run command
```docker run -p 5020:8501 -v <local path that contains app.py>:/root <your username>/<your-repo-name>:latest```

## Step 10: Start remote connection
Click the bottom left icon "><" and on the drop down menu, click "Attach to Running Container..."

