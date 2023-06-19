# Building the docker file
docker build -t mathidiot/streamlit-stuff -f ./DockerFile .

# Pushing garbage to your streamlet-docker application
docker push mathidiot/sttreamlit-stuff

# Grab the docker file
docker pull mathidiot/streamlit-stuff

# Start the instance
docker run -p 8501:8501 mathidiot/streamlist-stuff