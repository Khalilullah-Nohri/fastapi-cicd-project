pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "khalilullah59/fastapi-cicd-project:latest"
        DOCKER_SOCKET = "unix:///var/run/docker.sock"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Khalilullah-Nohri/fastapi-cicd-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🔧 Building Docker image using host Docker..."
                sh "docker -H ${DOCKER_SOCKET} build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Run Unit Tests (inside app image)') {
            steps {
                echo "🧪 Running tests inside the app image..."
                sh """
                docker run --rm \
                  -w /app \
                  -e PYTHONPATH=/app \
                  ${DOCKER_IMAGE} sh -c "
                    pip install --upgrade pip pytest && \
                    pip install -r requirements.txt && \
                    pytest code/tests/ --maxfail=1 --disable-warnings -q
                  "
                """
            }
        }

        stage('Login & Push to Docker Hub') {
            steps {
                echo "📦 Pushing image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh """
                    echo "$DOCKERHUB_PASS" | docker -H ${DOCKER_SOCKET} login -u "$DOCKERHUB_USER" --password-stdin
                    docker -H ${DOCKER_SOCKET} push ${DOCKER_IMAGE}
                    docker -H ${DOCKER_SOCKET} logout
                    """
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo "🚀 Deploying with docker-compose..."
                sh """
                DOCKER_HOST=${DOCKER_SOCKET} docker compose down || true
                DOCKER_HOST=${DOCKER_SOCKET} docker compose up -d --build
                """
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check console log for details."
        }
        always {
            cleanWs()
        }
    }
}
