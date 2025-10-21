pipeline {
    agent any   // use main Jenkins container

    environment {
        DOCKER_IMAGE = "khalilullah59/fastapi-cicd-project:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Khalilullah-Nohri/fastapi-cicd-project.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running tests inside Docker container..."
                sh """
                docker run --rm -v \$PWD:/app -w /app $DOCKER_IMAGE \
                /bin/bash -c "python3 -m venv myenv && \
                ./myenv/bin/pip install --upgrade pip && \
                ./myenv/bin/pip install -r requirements.txt && \
                ./myenv/bin/pytest code/tests/ --maxfail=1 --disable-warnings -q"
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t \$DOCKER_IMAGE ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Pushing image to Docker Hub..."
                withDockerRegistry([ credentialsId: 'docker-hub-cred', url: '' ]) {
                    sh "docker push \$DOCKER_IMAGE"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo "Deploying latest version..."
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
