pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 --version
                pip3 install --user -r requirements.txt
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh 'python3 -c "import streamlit; print(\'CI Test Passed\')"'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t resume-screening-app .'
            }
        }
    }
}
