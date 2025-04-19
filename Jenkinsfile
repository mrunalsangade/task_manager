pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/mrunalsangade/task_manager.git', credentialsId: 'f4bb4469-7e31-4cfc-a752-062d8c99b139'
      }
    }
    stage('Install Dependencies') {
      steps { 
        bat 'pip install -r requirements.txt'
      }
    }
    stage('Lint') {
      steps {
        bat 'flake8 .' 
      }
    }
    stage('Test') {
      steps {
        bat 'pytest --junitxml=reports/results.xml'
      }
      post {
        always {
          junit 'reports/results.xml'
        }
      }
    }
    stage('Docker Build & Push') {
      environment {
        DOCKERHUB_USR = credentials('mrunalsangade')
        DOCKERHUB_PSW = credentials('@Mrunal2705')
      }
      steps {
        bat """
          echo %DOCKERHUB_PSW% | docker login -u %DOCKERHUB_USR% --password-stdin
          docker build -t %DOCKERHUB_USR%/task_manager:latest .
          docker push %DOCKERHUB_USR%/task_manager:latest
        """
      }
    }
  }
}
