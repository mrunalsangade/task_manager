# TASK MANAGER
Task Manager Web Application


## Project Description

Task Manager is a lightweight Flask-based web application for managing to-do tasks. It stores tasks in a CSV file, offering a simple, portable solution for creating, viewing, editing, and deleting tasks through a clean user interface.

## CI/CT/CD Pipeline Flow

```text
[GitHub Push]
     ↓
[Jenkins] → Install dependencies → Run pytest → Build Docker image → Push to Docker Hub → Deploy container
```

1. **Continuous Integration:** A push to `main` on GitHub triggers Jenkins via webhook.
2. **Continuous Testing:** Jenkins installs Python packages and runs `pytest` to validate code.
3. **Continuous Deployment:** Upon passing tests, Jenkins builds and pushes a Docker image, then deploys it to the target environment.

## Setup & Run Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/mrunalsangade/task_manager.git
   cd task_manager
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python -m venv venv
   # Windows:
   venv\\Scripts\\activate
   # macOS/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the app locally**

   ```bash
   flask run
   ```

   Open `http://localhost:5000` in your browser.

## Docker Commands

1. **Build image**
   ```bash
   docker build -t task_manager:latest .
   ```
2. **Run container**
   ```bash
   docker run -d -p 5000:5000 --name task_manager task_manager:latest
   ```
3. **View logs**
   ```bash
   docker logs -f task_manager
   ```

