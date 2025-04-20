pipeline {
  agent any

  // Credentials for Docker Hub (ID’s must match what you created under Jenkins → Credentials)
  environment {
    DOCKERHUB_USR = credentials('mrunalsangade')
    DOCKERHUB_PSW = credentials('@Mrunal2705')
  }

  stages {
    stage('Checkout') {
      steps {
        // Uses the SCM settings from the Pipeline job
        checkout scm
      }
    }

    stage('Install Dependencies') {
      steps {
        // On Windows agents:
        bat 'pip install -r requirements.txt'
      }
    }

    stage('Lint') {
      steps {
        // Run your linter; adjust if you use a different tool
        bat 'flake8 .'
      }
    }

    stage('Build') {
      steps {
        // If you have a build step (e.g. compile, bundle), invoke it here.
        // For pure‑Python, this can be a no‑op:
        bat 'echo "No build step defined"'
      }
    }

    stage('Test') {
      steps {
        // Run pytest and generate JUnit XML for Jenkins
        bat 'pytest --junitxml=reports/results.xml'
      }
      post {
        always {
          // Publish test results
          junit 'reports/results.xml'
        }
      }
    }

    stage('Docker Build & Push') {
      steps {
        // Login, build, tag, and push
        bat """
          echo %DOCKERHUB_PSW% | docker login -u %DOCKERHUB_USR% --password-stdin
          docker build -t %DOCKERHUB_USR%/task_manager:latest .
          docker push %DOCKERHUB_USR%/task_manager:latest
        """
      }
    }
  }
}
