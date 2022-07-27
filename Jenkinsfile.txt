pipeline {
    agent any
    triggers{
         pollSCM("* * * * *")
    }
    stages {
        stage ("Unittest Test") {
            steps {
                sh "python test_calculator.py"
            }
        }

        stage ("Run Program") {
            steps {
                sh "python calculator.py"
            }
        }
    }
}