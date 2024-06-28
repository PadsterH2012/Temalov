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
                        // Build the Docker images using Docker Compose
                        sh 'docker-compose build'

                        // Push the Docker images to Docker Hub
                        sh 'docker-compose push'
                    }

                    // Log out from Docker Hub
                    sh 'docker logout'
                }
            }
        }

        stage('Run DB Tests') {
            steps {
                script {
                    echo "Running DB tests..."

                    // Start the services defined in the docker-compose file
                    dir('project_root') {
                        sh 'docker-compose up -d rpg_database'

                        // Wait for the database to start
                        sleep 20

                        // Run the DB tests
                        sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_db.py"'

                        // Stop and remove the database container
                        sh 'docker-compose down'
                    }
                }
            }
        }

        stage('Run Auth Tests') {
            steps {
                script {
                    echo "Running Auth tests..."

                    // Start the services defined in the docker-compose file
                    dir('project_root') {
                        sh 'docker-compose up -d rpg_database'

                        // Wait for the database to start
                        sleep 20

                        // Run the Auth tests
                        sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_auth.py"'

                        // Stop and remove the database container
                        sh 'docker-compose down'
                    }
                }
            }
        }

        stage('Run Character Tests') {
            steps {
                script {
                    echo "Running Character tests..."

                    // Start the services defined in the docker-compose file
                    dir('project_root') {
                        sh 'docker-compose up -d rpg_database'

                        // Wait for the database to start
                        sleep 20

                        // Run the Character tests
                        sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_characters.py"'

                        // Stop and remove the database container
                        sh 'docker-compose down'
                    }
                }
            }
        }

        // Add more stages as needed for other tests
    }
}
