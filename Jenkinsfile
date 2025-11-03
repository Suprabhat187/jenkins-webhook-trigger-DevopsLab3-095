pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build & Test Locally') {
            steps {
                echo 'Running Python locally (no Docker)...'
                bat '''
                REM Add Python to PATH temporarily for Jenkins
                set PATH=%PATH%;C:\\Users\\supi0\\AppData\\Local\\Programs\\Python\\Python312\\;C:\\Users\\supi0\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\

                python --version
                pip install -r requirements.txt
                python app.py
                '''
            }
        }
    }

    post {
        always {
            echo "Build complete: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
    }
}
