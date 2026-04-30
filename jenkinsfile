pipeline {
    agent any

    environment {
        IMAGE_NAME = "2024tm93613/aceest-gym-app"
        TAG = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                echo Installing dependencies
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo Running tests
                python -m pytest
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo Building Docker image
                docker build -t $IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                echo Pushing image to Docker Hub
                docker push $IMAGE_NAME:$TAG
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                echo Deploying to Kubernetes
                kubectl set image deployment/fitness-green fitness-container=$IMAGE_NAME:$TAG
                '''
            }
        }
    }
}