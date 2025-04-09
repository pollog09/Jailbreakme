# Jailbreakme

![WhatsApp Image 2025-04-08 at 16 48 40_3bb647ab](https://github.com/user-attachments/assets/81a4a28c-c3b1-4238-a17b-ca20ab94849f)


## Overview
Jailbreakme is a project designed to explore and demonstrate techniques for jailbraking AI LLMs, and exploring AI security in general.

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

