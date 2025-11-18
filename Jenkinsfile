def buildImage = {
    sh 'docker build -t incident-app .'
}

def runContainer = {
    sh 'docker run --rm incident-app'
}

pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }
    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    buildImage()
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    runContainer()
                }
            }
        }
    }
}
