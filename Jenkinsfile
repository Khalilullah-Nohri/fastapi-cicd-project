pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "khalilullah59/fastapi-cicd-project:latest"
        DOCKER_SOCKET = "unix:///var/run/docker.sock"
        K8S_DIR = "k8s"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Khalilullah-Nohri/fastapi-cicd-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🔧 Building Docker image..."
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
                    pytest code/tests/ -v -W default

                  "
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "📦 Pushing image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    echo "$PASS" | docker -H ${DOCKER_SOCKET} login -u "$USER" --password-stdin
                    docker -H ${DOCKER_SOCKET} push ${DOCKER_IMAGE}
                    docker -H ${DOCKER_SOCKET} logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "🚀 Deploying to Kubernetes..."
                sh """
                kubectl apply -f ${K8S_DIR}/mysql-deployment.yaml
                kubectl apply -f ${K8S_DIR}/deployment.yaml
                kubectl apply -f ${K8S_DIR}/service.yaml
                """
            }
        }
    }

    post {
        success {
            echo "✅ Deployed successfully to Kubernetes!"
        }
        failure {
            echo "❌ Pipeline failed. Check console logs."
        }
        always {
            cleanWs()
        }
    }
}
