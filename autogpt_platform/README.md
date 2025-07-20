# autogpt platform

a powerful system for creating and running ai agents to solve business problems. this platform enables you to harness the power of artificial intelligence to automate tasks, analyze data, and generate insights for your organization.

## getting started

### prerequisites

- docker
- docker compose v2 (comes with docker desktop, or can be installed separately)
- node.js & npm (for running the frontend application)

### running the system

to run the autogpt platform, follow these steps:

1. clone this repository to your local machine and navigate to the `autogpt_platform` directory within the repository:

```
git clone <https://github.com/cv55n/autogpt.git | git@github.com:cv55n/autogpt.git>
cd autogpt/autogpt_platform
```

2. run the following command:

```
cp .env.example .env
```

this command will copy the `.env.example` file to `.env`. you can modify the `.env` file to add your own environment variables.

3. run the following command:

```
docker compose up -d
```

this command will start all the necessary backend services defined in the `docker-compose.yml` file in detached mode.

4. navigate to `frontend` within the `autogpt_platform` directory:

```
cd frontend
```

you will need to run your frontend application separately on your local machine.

5. run the following command:

```
cp .env.example .env.local
```

this command will copy the `.env.example` file to `.env.local` in the `frontend` directory. you can modify the `.env.local` within this folder to add your own environment variables for the frontend application.

6. run the following command:

enable corepack and install dependencies by running:

```
corepack enable
pnpm i
```

generate the api client (this step is required before running the frontend):

```
pnpm generate:api-client
```

then start the frontend application in development mode:

```
pnpm dev
```

7. open your browser and navigate to `http://localhost:3000` to access the autogpt platform frontend.

## docker compose commands

here are some useful docker compose commands for managing your autogpt platform:

- `docker compose up -d`: start the services in detached mode.
- `docker compose stop`: stop the running services without removing them.
- `docker compose rm`: remove stopped service containers.
- `docker compose build`: build or rebuild services.
- `docker compose down`: stop and remove containers, networks, and volumes.
- `docker compose watch`: watch for changes in your services and automatically update them.

## sample scenarios

here are some common scenarios where you might use multiple docker compose commands:

1. updating and restarting a specific service:

```
pdating and restarting a specific service:
```

this rebuilds the `api_srv` service and restarts it without affecting other services.

2. viewing logs for troubleshooting:

```
docker compose logs -f api_srv ws_srv
```

this shows and follows the logs for both `api_srv` and `ws_srv` services.

3. scaling a service for increased load:

```
docker compose up -d --scale executor=3
```

this scales the `executor` service to 3 instances to handle increased load.

4. stopping the entire system for maintenance:

```
docker compose stop
docker compose rm -f
docker compose pull
docker compose up -d
```

this stops all services, removes containers, pulls the latest images, and restarts the system.

5. developing with live updates:

```
docker compose watch
```

this watches for changes in your code and automatically updates the relevant services.

6. checking the status of services:

```
docker compose ps
```

this shows the current status of all services defined in your `docker-compose.yml` file.

these scenarios demonstrate how to use docker compose commands in combination to manage your autogpt platform effectively.

## persisting data

to persist data for postgresql and redis, you can modify the `docker-compose.yml` file to add volumes. here's how:

1. open the `docker-compose.yml` file in a text editor.
2. add volume configurations for postgresql and redis services:

```yml
services:
  postgres:
    # ... outras configurações ...
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    # ... outras configurações ...
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

3. save the file and run `docker compose up -d` to apply the changes.

this configuration will create named volumes for postgresql and redis, ensuring that your data persists across container restarts.

## api client generation

the platform includes scripts for generating and managing the api client:

- `pnpm fetch:openapi`: fetches the openapi specification from the backend service (requires backend to be running on port 8006)
- `pnpm generate:api-client`: generates the typescript api client from the openapi specification using orval
- `pnpm generate:api-all`: runs both fetch and generate commands in sequence

### manual api client updates

if you need to update the api client after making changes to the backend api:

1. ensure the backend services are running:

```
docker compose up -d
```

2. generate the updated api client:

```
pnpm generate:api-all
```

this will fetch the latest openapi specification and regenerate the typescript client code.
