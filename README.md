# How to Run the Project with Docker Compose

## Prerequisites

1. **Install Docker**
   - For **Windows**, install [Docker Desktop](https://www.docker.com/products/docker-desktop).
   - For **Linux**, install [Docker based on your distribution](https://docs.docker.com/engine/install/).

2. **Verify Installation**
   - Check that Docker is running:
     ```bash
     docker --version
     ```
   - Check that Docker Compose is installed:
     ```bash
     docker compose version
     ```
     - **IMPORTANT**: Ensure that Docker Compose is version 2 or higher.

## Running the Project

1. **Clone the Repository**
   - Clone the project repository to your local machine:
     ```bash
     git clone https://github.com/JoeEnan/stt-transcripts-search.git
     cd stt-transcripts-search
     ```

2. **Build and Run Docker Containers**
   - After cloning the repository, ensure the `run.sh` script is executable by running:

    ```bash
    chmod +x run.sh
    ```

    - Then run the `run.sh` file
    ```bash
    ./run.sh
    ```

    - Note: You can add the `-d` flag to run the container in detached mode

## Example traefik config:
- Just update the `rmbg.local.com` portions of the labels, ensure you have traefik container setup already
```yml
services:
  bg_removal:
    networks:
      - proxy
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.rmbg.entrypoints=http"
      - "traefik.http.routers.rmbg.rule=Host(`rmbg.local.com`)"
      - "traefik.http.middlewares.rmbg-https-redirect.redirectscheme.scheme=https"
      - "traefik.http.routers.rmbg.middlewares=rmbg-https-redirect"
      - "traefik.http.routers.rmbg-secure.entrypoints=https"
      - "traefik.http.routers.rmbg-secure.rule=Host(`rmbg.local.com`)"
      - "traefik.http.routers.rmbg-secure.tls=true"
      - "traefik.http.services.rmbg.loadbalancer.server.port=8501"
      - "traefik.docker.network=proxy"

networks:
  proxy:
    external: true

```