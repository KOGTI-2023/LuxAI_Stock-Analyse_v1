# LuxAi_AI-Stock-Predict_App

This application uses Docker Compose to manage its services. 

## Using Docker Compose

To start the services defined in the `docker-compose.yml` file, navigate to the root directory of the repository and run the following command:

```
docker-compose up
```

To check if the `docker-compose.yml` file is syntactically correct, run the following command:

```
docker-compose config
```

## Services

The main application service is defined in the `docker-compose.yml` file. 

## Environment Variables

The `docker-compose.yml` file defines several environment variables that can be set as needed.

## Ports

The services expose several ports for communication. Refer to the `docker-compose.yml` file for the specific ports used by each service.

## Volumes

Data volumes are defined in the `docker-compose.yml` file. These volumes are used to persist data across container restarts.

## Dependencies

The `docker-compose.yml` file defines several dependencies as separate services. These services must be running for the main application to function correctly.

## Committing and Pushing Changes

To commit and push changes to the repository, use the following commands:

```
git add .
git commit -m "Your commit message"
git push
```

Please replace "Your commit message" with a meaningful description of the changes you made.