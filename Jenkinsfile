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

        stage ("Deploy to Staging") {
            steps {
                sh 'docker compose up -f docker-compose.yml -d'
            }
        }

        stage ("Acceptance test") {
            steps {
                sh 'docker compose up -f docker-compose.yml -f acceptance/docker-compose-acceptance.yml build test'
                sh 'docker compose -f docker-compose.yml -f acceptance/docker-compose-acceptance.yml -p acceptance up -d'
                sh 'test $(curl docker wait acceptance_test_1) -eq 0'
            }
        }
    }

    post {
        always {
            sh "docker-compose -f docker-compose.yml -f acceptance/docker-compose-acceptance.yml -p acceptance down"
        }
    }
}