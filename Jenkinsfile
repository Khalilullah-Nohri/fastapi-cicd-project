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

        stage('Run Unit Tests (inside app image)') {
            steps {
                echo "Running tests inside the app image (uses image's Python)..."
                sh """
                # ensure we explicitly use the host docker socket (avoid TCP env):
                docker -H ${DOCKER_SOCKET} run --rm \\
                  -v \$PWD:/app -w /app \\
                  ${DOCKER_IMAGE} /bin/bash -lc "python3 -m venv myenv && \
                  ./myenv/bin/pip install --upgrade pip && \
                  ./myenv/bin/pip install -r requirements.txt && \
                  ./myenv/bin/pytest code/tests/ --maxfail=1 --disable-warnings -q"
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image (using host docker via socket)..."
                sh "docker -H ${DOCKER_SOCKET} build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Login & Push to Docker Hub') {
            steps {
                echo "Logging in and pushing image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh """
                    docker -H ${DOCKER_SOCKET} login -u "$DOCKERHUB_USER" -p "$DOCKERHUB_PASS"
                    docker -H ${DOCKER_SOCKET} push ${DOCKER_IMAGE}
                    docker -H ${DOCKER_SOCKET} logout
                    """
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo "Deploying using docker compose (host docker socket)..."
                sh """
                # use the host docker socket for compose as well
                DOCKER_HOST=${DOCKER_SOCKET} docker compose down
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
