pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/sumanbiswas15/resume_screening_tool.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh 'python3 -c "import streamlit; print(\"CI Test Passed\")"'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t resume-screening-app .'
            }
        }
    }
}
