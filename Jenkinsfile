pipeline {
    agent any
    triggers{
         pollSCM("* * * * *")
    }
    stages {

        stage ("Docker Build") {
            steps {
                sh 'docker build --no-cache -t calculator .'
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

        stage ("Acceptance test") {
            steps {
                sleep 60
                sh "/home/node01/jenkins_cicd/chap4/acceptance_test.sh"
            }
        }
    }
}