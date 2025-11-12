pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/<Sundari-p>/doctor-appointment-devops.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t doctor-appointment .'
            }
        }
        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 doctor-appointment'
            }
        }
    }
}