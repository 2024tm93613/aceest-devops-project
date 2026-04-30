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

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat '''
                    echo Logging into Docker Hub
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    '''
                }
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
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    bat '''
                    echo Deploying to Kubernetes

                    kubectl config use-context minikube
                    kubectl get nodes

                    kubectl set image deployment/fitness-green fitness-container=%IMAGE_NAME%:%TAG%
                    '''
            }
        }
    }
}