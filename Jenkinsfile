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
            parallel {
                stage('Build Database Image') {
                    steps {
                        script {
                            sh "docker build -t ${DOCKER_HUB_REPO}:rpg_database -f project_root/rpg_database/Dockerfile ."
                            sh "docker push ${DOCKER_HUB_REPO}:rpg_database"
                        }
                    }
                }
                stage('Build Web Frontend Image') {
                    steps {
                        script {
                            sh "docker build -t ${DOCKER_HUB_REPO}:rpg_web_frontend -f project_root/rpg_web_frontend/Dockerfile ."
                            sh "docker push ${DOCKER_HUB_REPO}:rpg_web_frontend"
                        }
                    }
                }
                stage('Build Content Creator Image') {
                    steps {
                        script {
                            sh "docker build -t ${DOCKER_HUB_REPO}:rpg_content_creator -f project_root/rpg_content_creator/Dockerfile ."
                            sh "docker push ${DOCKER_HUB_REPO}:rpg_content_creator"
                        }
                    }
                }
                stage('Build Content API Image') {
                    steps {
                        script {
                            sh "docker build -t ${DOCKER_HUB_REPO}:rpg_content_api -f project_root/rpg_content_api/Dockerfile ."
                            sh "docker push ${DOCKER_HUB_REPO}:rpg_content_api"
                        }
                    }
                }
            }
        }

        stage('Run Tests') {
            parallel {
                stage('DB Tests') {
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
                stage('Auth Tests') {
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
                stage('Character Tests') {
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
    }
}
