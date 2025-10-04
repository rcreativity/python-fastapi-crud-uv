# FastAPI Project Setup Guide
FastAPI Project Setup Guide

# 🚀 Overview
This repository contains a Python project built with FastAPI and uses Uvicorn as the ASGI server. This guide details the steps required to set up the project environment using the high-performance package manager, uv, and run the application locally.

# 🛠️ Requirements
- Python 3.13+
- uv (recommended for installation and dependency management)

# 💻 Project Setup and Execution
Follow these steps in your terminal to get the project up and running.

### 1. Initialize the Virtual Environment
Use `uv init` to create an isolated Python virtual environment named .venv in the current directory.

> uv init .

### 2. Install Dependencies
Add the necessary packages (fastapi and uvicorn) to your environment.

> uv add fastapi uvicorn

### 3. Activate the Environment
Activate the virtual environment to ensure all subsequent commands use the correct project dependencies.

> source .venv/bin/activate


### 4. Run the Application
Start the FastAPI server, loading the application instance named app from main.py. The ```--reload``` flag ensures the server automatically restarts when you make code changes.

> uvicorn main:app --reload

The application will now be running, typically accessible at http://127.0.0.1:8000.

### 5. Access the API Documentation

Once the server is running, you can access the interactive documentation provided by FastAPI to explore the available endpoints:

- Swagger UI: ```http://127.0.0.1:8000/docs```

- ReDoc: ```http://127.0.0.1:8000/redoc```

### 6. 🚪 Exiting the Virtual Environment
When you are finished working on the project, run the deactivate command to exit the virtual environment and return to your system's global environment.

> deactivate
