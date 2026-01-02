pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies'
            }
        }

        stage('Test Application') {
            steps {
                echo 'Running tests'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t resume-screening-app .'
            }
        }
    }
}

