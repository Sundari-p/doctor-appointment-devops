pipeline {
    agent any

    environment {
        IMAGE_NAME = "doctor-appointment-app"
        CONTAINER_NAME = "doctor-app"
        PORT = "8085"
    }

    stages {

       

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Stop Old Container') {
            steps {
                echo 'Stopping any running containers...'
                bat "docker stop %CONTAINER_NAME% || exit 0"
                bat "docker rm %CONTAINER_NAME% || exit 0"
            }
        }

        stage('Run New Container') {
            steps {
                echo 'Starting new Docker container...'
                bat "docker run -d -p %PORT%:%PORT% --name %CONTAINER_NAME% %IMAGE_NAME%"
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Verifying container is running...'
                bat "docker ps"
            }
        }
    }

    post {
        success {
            echo "✅ Deployment completed successfully!"
        }
        failure {
            echo "❌ Something went wrong. Check the logs."
        }
    }
}