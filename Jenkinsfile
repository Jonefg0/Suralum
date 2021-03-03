pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker-composer build --no-cache'
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose up -d --force-recreate'
            }
        }
    }
}
