pipeline {
  agent any

  stages {
    stage('Clone Repo') {
      steps {
        echo 'Cloning repository from GitHub (dev branch)...'
        git branch: 'dev',
            credentialsId: 'github-creds',
            url: 'https://github.com/manojgk0210-hue/flask-mysql-register.git'
        echo 'Repository cloned successfully.'
      }
    }

    stage('Build Docker Image') {
      steps {
        echo 'Building Docker images using docker-compose...'
        sh 'docker-compose build'
        echo 'Docker image build completed.'
      }
    }

    stage('Run Containers') {
      steps {
        echo 'Starting Docker containers...'
        sh 'docker-compose up -d'
        echo 'Docker containers are running.'
      }
    }
  }
}
