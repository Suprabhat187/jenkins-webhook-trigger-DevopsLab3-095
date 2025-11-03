pipeline {
  agent any
  environment {
    IMAGE_NAME = "weather-monitor:${env.BUILD_NUMBER}"
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build("${IMAGE_NAME}")
        }
      }
    }
    stage('Run Smoke Test') {
      steps {
        script {
          // run a quick smoke container and stop it - optional
          def c = dockerImage.run("-d --name smoke_${env.BUILD_NUMBER}")
          sh "sleep 3"
          sh "docker logs smoke_${env.BUILD_NUMBER} || true"
          sh "docker rm -f smoke_${env.BUILD_NUMBER} || true"
        }
      }
    }
    stage('Archive') {
      steps {
        archiveArtifacts artifacts: 'Dockerfile, Jenkinsfile, **/*.py', fingerprint: true
      }
    }
  }
  post {
    always {
      echo "Build finished: ${currentBuild.fullDisplayName}"
    }
  }
}
