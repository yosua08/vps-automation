pipeline {
    agent {
        node {
            label 'linux'
        }
    }

    stages {
        stage ('Test') {
            steps {
                sh 'sudo ufw status'
            }
        }
    }

    post {
        always {
            echo 'Always send response'
        }

        success {
            echo 'Success build job'
        }

        failure {
            echo 'Job failed to build'
        }

        cleanup {
            echo 'Dont care success or failure'
        }
    }
}