# Creating a Docker account
Go to the following website and create an account with github if you haven't already.

```https://hub.docker.com/```

# What Now?

### Creating a Docker Repository
- #### Go ahead and click that fancy shmancy "Create repository" button and name it whatever you want
![](./images/create_repo.png)

- #### Once you do that, you will get a docker repository similar to the one you see above, where it's your docker username, followed by the name of the repository.

### Building the docker file
- #### Now we have to build the docker file to port it to our brand new repository.
- #### We do this by using our DockerFile, which you can browse
```docker build -t username/docker-repository -f ./Dockerfile .```

### Pushing garbage to your streamlet-docker application
```docker push username/docker-repository```
```

```

# Grab the docker file
```docker pull username/repository-name```

# Start the instance
```docker run -p 8501:8501 username/repository-name```

# Launch the server under your localhost
http://localhost:8501/