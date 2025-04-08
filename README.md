# Jailbreakme

## Overview
Jailbreakme is a project designed to explore and demonstrate techniques for customizing and extending device functionality. This repository contains code, documentation, and resources for educational purposes.

## Features
- Customization tools
- Device optimization techniques
- Educational resources

## Installation
1. Clone the repository:
    ```bash
    git clone {repourl}
    ```
2. Navigate to the project directory:
    ```bash
    cd Jailbreakme
    ```
3. Build and start the services using Docker Compose:
    ```bash
    docker-compose up -d --build
    ```
4. Pull the required model:
    ```bash
    docker exec -it jailbreakme-ollama-1 ollama pull mistral
    ```

## Usage
### Access the Chat Interface
Once the model is downloaded, open your browser and go to:

```http://localhost:5000```

