pipeline {
    agent any
    triggers{
         pollSCM("* * * * *")
    }
    stages {

        stage ("Docker Build") {
            steps {
                sh 'docker build -t --no-cache calculator .'
                sh 'docker tag calculator 192.168.1.29:5000/calculator'
            }
        }

        stage ("Docker Push") {
            steps {
                sh 'docker push 192.168.1.29:5000/calculator'
            }
        }

        stage ("Deploy to Staging") {
            steps {
                sh 'docker rm -f calculator'
                sh 'docker run -d -p 8001:8001 --name calculator 192.168.1.29:5000/calculator'
            }
        }
    }
}