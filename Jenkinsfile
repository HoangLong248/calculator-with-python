pipeline {
    agent any
    triggers{
         pollSCM("* * * * *")
    }
    stages {
        stage ("Unittest Test") {
            steps {
                sh 'python3 test_calculator.py'
            }
        }

        stage ("Run Program") {
            steps {
                sh 'python3 calculator.py'
            }
        }
    }
}