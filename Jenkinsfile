pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        DOCKER_HUB_REPO = 'padster2012'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                script {
                    // Change to project_root directory
                    dir('project_root') {
                        // Build the Docker images using Docker Compose
                        sh 'docker-compose build'
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

                            // Start all the services defined in the docker-compose file
                            dir('project_root') {
                                sh 'docker-compose up -d'

                                // Wait for the services to start
                                sleep 20

                                // Run the DB tests
                                sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_db.py"'

                                // Stop and remove all the containers
                                sh 'docker-compose down'
                            }
                        }
                    }
                }

                // stage('Auth Tests') {
                //     steps {
                //         script {
                //             echo "Running Auth tests..."

                //             // Start all the services defined in the docker-compose file
                //             dir('project_root') {
                //                 sh 'docker-compose up -d'

                //                 // Wait for the services to start
                //                 sleep 20

                //                 // Run the Auth tests
                //                 sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_auth.py"'

                //                 // Stop and remove all the containers
                //                 sh 'docker-compose down'
                //             }
                //         }
                //     }
                // }

                // stage('Character Tests') {
                //     steps {
                //         script {
                //             echo "Running Character tests..."

                //             // Start all the services defined in the docker-compose file
                //             dir('project_root') {
                //                 sh 'docker-compose up -d'

                //                 // Wait for the services to start
                //                 sleep 20

                //                 // Run the Character tests
                //                 sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_characters.py"'

                //                 // Stop and remove all the containers
                //                 sh 'docker-compose down'
                //             }
                //         }
                //     }
                // }

                // stage('Quest Tests') {
                //     steps {
                //         script {
                //             echo "Running Quest tests..."

                //             // Start all the services defined in the docker-compose file
                //             dir('project_root') {
                //                 sh 'docker-compose up -d'

                //                 // Wait for the services to start
                //                 sleep 20

                //                 // Run the Quest tests
                //                 sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_quests.py"'

                //                 // Stop and remove all the containers
                //                 sh 'docker-compose down'
                //             }
                //         }
                //     }
                // }

                // stage('Game Tests') {
                //     steps {
                //         script {
                //             echo "Running Game tests..."

                //             // Start all the services defined in the docker-compose file
                //             dir('project_root') {
                //                 sh 'docker-compose up -d'

                //                 // Wait for the services to start
                //                 sleep 20

                //                 // Run the Game tests
                //                 sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_games.py"'

                //                 // Stop and remove all the containers
                //                 sh 'docker-compose down'
                //             }
                //         }
                //     }
                // }

                // stage('Settings Tests') {
                //     steps {
                //         script {
                //             echo "Running Settings tests..."

                //             // Start all the services defined in the docker-compose file
                //             dir('project_root') {
                //                 sh 'docker-compose up -d'

                //                 // Wait for the services to start
                //                 sleep 20

                //                 // Run the Settings tests
                //                 sh 'docker-compose run --rm rpg_web_frontend python -m unittest discover -s tests -p "test_settings.py"'

                //                 // Stop and remove all the containers
                //                 sh 'docker-compose down'
                //             }
                //         }
                //     }
                // }
            }
        }
    }

    post {
        success {
            script {
                // Log in to Docker Hub
                sh "echo \$DOCKERHUB_CREDENTIALS_PSW | docker login -u \$DOCKERHUB_CREDENTIALS_USR --password-stdin"

                // Change to project_root directory
                dir('project_root') {
                    // Push the Docker images to Docker Hub using Docker Compose
                    sh 'docker-compose push'
                }

                // Log out from Docker Hub
                sh 'docker logout'
            }
        }
    }
}
