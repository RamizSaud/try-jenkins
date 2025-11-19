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
            options {
                timeout(time: 100, unit: 'SECONDS')
            }
        }

        stage('Run Container') {
            steps {
                script {
                    def userInput = input(
                        id: 'userInputId',
                        message: 'Please Provide JSON Config Text:',
                        ok: 'Proceed',
                        parameters: [
                            text(
                                name: 'Config',
                                defaultValue: '',
                                description: 'Enter Config Text (multiline allowed)'
                            )
                        ]
                    )
                    echo("User Provided Config Text: ${userInput}")
                    runContainer()
                }
            }
        }
    }
}
