pipeline {
    agent any
    triggers{
         pollSCM("* * * * *")
    }
    stages {

        stage ("Docker Build") {
            steps {
                sh 'docker build -t calculator .'
                sh 'docker tag calculator 192.168.1.29:5000/calculator'
            }
        }

        stage ("Docker Push") {
            steps {
                sh 'docker push 192.168.1.29:5000/calculator'
            }
        }
    }
}