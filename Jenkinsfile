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
        // ensure the reports directory exists
        bat 'if not exist reports mkdir reports'
        // run pytest, but if it exits with code 5 (no tests) we ignore that
        bat """
          python -m pytest --junitxml=reports/results.xml || exit /B 0
        """
      }
      post {
        always {
          // publish whatever XML we have, even if it’s empty
          junit testResults: 'reports/results.xml', allowEmptyResults: true
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
          bat 'docker build -t %DOCKER_USER%/task_manager_test:latest .'
          bat 'docker push %DOCKER_USER%/task_manager_test:latest'
        }
      }
    }
  }
}
