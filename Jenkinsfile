pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clones your GitHub repo
                git 'https://github.com/sumanbiswas15/resume_screening_tool.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Installs Python dependencies
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                // Simple test to ensure Streamlit loads
                sh 'python3 -c "import streamlit; print(\"CI Test Passed\")"'
            }
        }

        stage('Docker Build') {
            steps {
                // Builds Docker image from Dockerfile
                sh 'docker build -t resume-screening-app .'
            }
        }
    }
}

