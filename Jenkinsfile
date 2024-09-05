pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('user_service', './services/user_service')
                }
            }
        }
        stage('Test') {
            steps {
                // Add your test steps here
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.image('user_service').run('-p 5001:5001')
                }
            }
        }
    }
}