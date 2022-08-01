pipeline {
    agent any
    triggers{
         pollSCM("* * * * *")
    }
    stages {

        stage ("Docker Build") {
            steps {
                sh 'docker compose -f docker-compose.yml build'
            }
        }

        stage ("Docker Push") {
            steps {
                sh 'docker compose push calculator'
            }
        }

        stage ("Docker Deploy") {
            steps {
                sh 'docker compose -f docker-compose.yml up -d'
            }
        }
        stage ("Acceptance test") {
            steps {
                sh 'docker compose -f docker-compose.yml -f acceptance/docker-compose-acceptance.yml build test'
                sh 'docker compose -f acceptance/docker-compose-acceptance.yml -p acceptance up -d'
                sh 'test $(docker wait acceptance-test-1) -eq 0'
            }
        }

    post {
        always {
            sh "docker compose -f acceptance/docker-compose-acceptance.yml -p acceptance down"
            sh "docker compose -f docker-compose.yml down"
        }
    }
}