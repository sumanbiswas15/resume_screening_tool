pipeline {
    agent any

    environment {
        IMAGE_NAME = "sumanbiswas22/resume-screening-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python venv & Install Deps') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh '''
                docker push $IMAGE_NAME:latest
                '''
            }
        }
    }
}

