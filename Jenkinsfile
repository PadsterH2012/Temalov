pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS  = credentials('dockerhub-credentials-id')
        DOCKER_HUB_REPO  = 'padster2012/temalov'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }

        stage('Build and Push Images') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh "echo \$DOCKERHUB_CREDENTIALS_PSW | docker login -u \$DOCKERHUB_CREDENTIALS_USR --password-stdin"

                    // Change to project_root directory
                    dir('project_root') {
                        // Build and push the Docker images using Docker Compose
                        sh 'ls'
                        sh 'docker-compose -f docker-compose.yml build'
                        sh 'docker-compose -f docker-compose.yml push'
                    }

                    // Log out from Docker Hub
                    sh 'docker logout'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests..."

                    // Start the services defined in the docker-compose file
                    dir('project_root') {
                        sh 'docker-compose up -d rpg_database'

                        // Wait for the database to start
                        sleep 20

                        // Run the tests
                        sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests'

                        // Stop and remove the database container
                        sh 'docker-compose down'
                    }
                }
            }
        }
    }
}
