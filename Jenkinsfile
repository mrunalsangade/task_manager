pipeline {
  agent any

  environment {
    // Replace with your Jenkins-stored Docker Hub credentials ID
    DOCKERHUB_CRED = 'f4bb4469-7e31-4cfc-a752-062d8c99b139'
  }

  stages {
    /* Default “Checkout SCM” is handled automatically */

    stage('Install Dependencies') {
      steps {
        // Make sure pip is up to date
        bat 'python -m pip install --upgrade pip'
        // Install from requirements.txt
        bat 'python -m pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        // create a folder for test reports
        bat 'if not exist reports mkdir reports'
        // Run pytest and produce JUnit XML for reporting
        bat 'python -m pytest --junitxml=reports/results.xml || exit 0'
      }
      post {
        always {
          // Publish test results in Jenkins
          junit 'reports/results.xml'
        }
      }
    }

    stage('Build') {
      steps {
        // Placeholder for any build step; Python projects often don't need this
        bat 'echo "No build step defined"'
      }
    }

    stage('Docker Build & Push') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: "${DOCKERHUB_CRED}",
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          // Log in, build, tag & push your image
          bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
          bat 'docker build -t %DOCKER_USER%/task_manager:latest .'
          bat 'docker push %DOCKER_USER%/task_manager:latest'
        }
      }
    }
  }
}
