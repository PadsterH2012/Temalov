pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        DOCKER_HUB_REPO = 'padster2012/temalov'
    }

    stages {
        stage('log into docker hub') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                    }
                }
            }
        }
        stage('Build Database Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_REPO}:rpg_database ./rpg_database"
                }
            }
        }
        
        stage('Build Web Frontend Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_REPO}:rpg_web_frontend ./rpg_web_frontend"
                }
            }
        }
        
        stage('Build Content Creator Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_REPO}:rpg_content_creator ./rpg_content_creator"
                }
            }
        }
        
        stage('Build Content API Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_REPO}:rpg_content_api ./rpg_content_api"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run database service
                    sh "docker run -d --name rpg_database -e POSTGRES_DB=rpg -e POSTGRES_USER=rpg_user -e POSTGRES_PASSWORD=rpg_pass -p 5432:5432 ${DOCKER_HUB_REPO}:rpg_database"
                    // Wait for database to start
                    sleep 20
                    // Run tests
                    sh "docker run --rm --network=host ${DOCKER_HUB_REPO}:rpg_web_frontend python -m unittest discover -s tests"
                    // Stop and remove the database container
                    sh "docker stop rpg_database"
                    sh "docker rm rpg_database"
                }
            }
        }

        /*
        stage('Push Images') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'DOCKER_HUB_CREDENTIALS') {
                        def services = ['rpg_database', 'rpg_web_frontend', 'rpg_content_creator', 'rpg_content_api']
                        services.each { service ->
                            sh "docker tag ${DOCKER_HUB_REPO}:${service} ${DOCKER_HUB_REPO}:${service}-latest"
                            sh "docker push ${DOCKER_HUB_REPO}:${service}-latest"
                        }
                    }
                }
            }
        }
        */
    }
}
