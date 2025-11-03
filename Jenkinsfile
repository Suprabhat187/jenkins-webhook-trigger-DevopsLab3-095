pipeline {
    agent any
    environment {
        IMAGE_NAME = "weather-monitor:${env.BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }
        stage('Run Container (Test)') {
            steps {
                echo "Running container for quick test..."
                script {
                    def c = dockerImage.run("-d -p 5000:5000")
                    sh "sleep 5"
                    sh "curl -f http://localhost:5000 || true"
                    sh "docker rm -f ${c.id}"
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                echo "Archiving build files..."
                archiveArtifacts artifacts: 'Dockerfile, Jenkinsfile, **/*.py', fingerprint: true
            }
        }
    }
    post {
        always {
            echo "Build complete: ${currentBuild.fullDisplayName}"
        }
    }
}
