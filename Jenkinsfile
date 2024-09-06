pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t user_service ./services/user_service'
                sh 'docker build -t order_service ./services/order_service'
            }
        }
        stage('Test') {
            steps {
                sh 'chmod +x health_check.sh'
                sh './health_check.sh'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop user_service || true'
                sh 'docker rm user_service || true'
                sh 'docker run -d --name user_service -p 5001:5001 user_service'
                
                sh 'docker stop order_service || true'
                sh 'docker rm order_service || true'
                sh 'docker run -d --name order_service -p 5002:5002 order_service'
            }
        }
    }
}

