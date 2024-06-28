pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS  = credentials('dockerhub-credentials-id')
        DOCKER_ HUB_REPO  = 'padster2012/temalov'
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

                    // Change to project-root directory
                    dir('project-root') {
                        // Build and push the Docker images using Docker Compose
                        sh 'docker-compose  -f docker-compose-build.yml build'
                        sh 'docker-compose  -f docker-compose-build.yml push'
                    }

                    // Log out from Docker Hub
                    sh 'docker logout'
                }
            }
        }

        stage('Log into Docker Hub') {
            steps{
                script   { echo "Logging into Docker Hub..." }
            }
        }

        stage('Build the Database Image') {
            steps{
                script  { echo "Building database image..." }
            }
        }

        stage('Build the Web Frontend Image') {
            steps{
                script  { echo "Building web frontend image..." }
            }
        }

        stage('Build the Content Creator Image') {
            steps{
                script  { echo "Building content creator image..." }
            }
        }

        stage('Build the Content API Image') {
            steps{
                script  { echo "Building content API image..." }
            }
        }

        stage('Run Tests') {
            steps{
                script {
                    echo "Running tests..."

                    // Spin up a database service with specified env vars.
                    docker.image('mysql:latest').withEnv(['MYSQL_ROOT_PASSWORD=root', 'MYSQL_DATABASE=test']).run()

                    // Run an interactive container for the duration of test suite's execution.
                    docker.run('-e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test --rm --name test-container -v $WORKSPACE:/home/mysql/ localtest.sh')
                }
            }
        }

        stage('Stop and Remove Database Container') {
            steps{
                script { echo "Stopping and removing the database container..." }
            }
        }
    }
}