pipeline {
    agent any

    stages {

        stage('Setup Python Venv') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                . venv/bin/activate
                python3 -c "import streamlit; print('CI Test Passed')"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t resume-screening-app .'
            }
        }
    }
}
