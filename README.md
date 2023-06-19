# DO NOT RUN

### Building the docker file
```docker build -t username/docker-repository -f ./DockerFile .```

### Pushing garbage to your streamlet-docker application
```docker push username/docker-repository```

# YOU CAN RUN THESE 2

# Grab the docker file
```docker pull mathidiot/streamlit-stuff```

# Start the instance
```docker run -p 8501:8501 mathidiot/streamlit-stuff```

# Launch the server under your localhost
http://localhost:8501/