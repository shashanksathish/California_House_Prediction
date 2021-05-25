# California_House_Prediction

This is a Dockerized Version of the Machine Learning Application to calculate the pricing of the California Housing with a Front End GUI, the model's backend is performed by Flask.

## Installation
Download the [Docker](https://www.docker.com/products/docker-desktop) and make sure all the requirements are satisfied.

## Running on Docker
After the docker is installed, open a CLI use the below commands.

```bash
docker build -t <App_Name>:<Version> .
```

The above command should be executed once the docker starts to run, it creates a docker images with the title (-t) specified. This might take a couple of minutes since the machine needs to download the  python from the docker hub and install all the dependencies.

After creating the images,

```bash
docker run -d -p 5000:5000 <App_Name>:<Version>
```

Once done go to the [localhost](http://127.0.0.1:5000/) to see the Machine Learning Model containarized.
