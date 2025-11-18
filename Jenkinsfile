def buildImage = {
    sh 'docker build -t incident-app .'
}

def runContainer = {
    def userInput = input(
                        id: 'userInputId',
                        message: 'Please provide detailed comments:',
                        ok: 'Proceed',
                        parameters: [
                            text(
                                name: 'comments',
                                defaultValue: 'Enter multiline text here...',
                                description: 'Enter comments or a configuration snippet (multiline allowed)'
                            )
                        ]
                    )
                    // The submitted value is stored in the 'userInput' variable
                    echo "User provided comments: ${userInput.comments}"
                    
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
