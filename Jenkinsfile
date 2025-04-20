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
        // make sure reports folder exists
        bat 'if not exist reports mkdir reports'

        // explicitly run pytest on the tests/ folder
        bat 'python -m pytest tests --maxfail=1 --disable-warnings --junitxml=reports/results.xml'
      }
      post {
        always {
          // this will fail the build if the XML is malformed or missing tests
          junit allowEmptyResults: false, testResults: 'reports/results.xml'
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
