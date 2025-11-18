pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t incident-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm incident-app'
            }
        }
    }
}
