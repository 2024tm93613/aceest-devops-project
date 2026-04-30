pipeline {
    agent any

    environment {
        IMAGE_NAME = "2024tm93613/aceest-gym-app"
        TAG = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                echo Installing dependencies
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                echo Running tests
                python -m pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                echo Building Docker image
                docker build -t %IMAGE_NAME%:%TAG% .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                bat '''
                echo Pushing image
                docker push %IMAGE_NAME%:%TAG%
                '''
            }
        }

        stage('Deploy to Kubernetes') {
                withCredentials([usernamePassword(
                credentialsId: 'docker-hub-creds',
                usernameVariable: '2024tm93613',
                passwordVariable: 'Rajit@2512'
            )])
            steps {
                bat '''
                echo Deploying
                kubectl set image deployment/fitness-green fitness-container=%IMAGE_NAME%:%TAG%
                '''
            }
        }
    }
}