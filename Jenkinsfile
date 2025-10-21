pipeline {
    agent {
        docker { image 'python:3.11-slim' }
    }

    environment {
        DOCKER_IMAGE = "khalilullah59/fastapi-cicd-project:latest"
        PYTHON = "./myenv/bin/python3"
        PIP = "./myenv/bin/pip"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Khalilullah-Nohri/fastapi-cicd-project.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv myenv'
                sh '${PIP} install --upgrade pip'
                sh '${PIP} install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running pytest unit tests..."
                sh './myenv/bin/pytest code/tests/ --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Pushing image to Docker Hub..."
                withDockerRegistry([ credentialsId: 'docker-hub-cred', url: '' ]) {
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo "Deploying new version..."
                sh "docker compose down"
                sh "docker compose up -d --build"
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs."
        }
        always {
            cleanWs()
        }
    }
}
