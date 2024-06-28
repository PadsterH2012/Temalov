pipeline  {

    agent any

    environment  {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        DOCKER_HUB_REPO = 'padster2012/temalov'
     }

    stages  {

        stage('Checkout Code')  {
            steps {
                // Checkout the repository
                checkout scm
            }
         }

        stage('Build and Push Images') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"

                    // Change to project-root directory
                    dir('project-root') {
                        // Build and push the Docker images using Docker Compose
                        sh 'docker-compose -f docker-compose-build.yml build'
                        sh 'docker-compose -f docker-compose-build.yml push'
                    }

                    // Log out from Docker Hub
                    sh 'docker logout'
                }
            }
        }

         // Log into Docker Hub
        stage('Log into Docker Hub')  {
             steps{
                script  {
                    echo "Logging into Docker Hub..."
                 }
             }
         }

        // Build the Database Image
        stage('Build Database Image')  {
            steps{
                script  {
                    echo "Building database image..."
                 }
             }
         }

        // Build the Web Frontend Image
        stage('Build Web Frontend Image')  {
            steps{
                script  {
                    echo "Building web frontend image..."
                 }
             }
         }

        // Build the Content Creator Image
        stage('Build Content Creator Image')  {
            steps{
                script  {
                    echo "Building content creator image..."
                 }
             }
         }

        // Build the Content API Image
        stage('Build Content API Image')  {
            steps{
                script  {
                    echo "Building content API image..."
                 }
             }
         }

         // Run Tests against the built Docker Images
         stage('Run Tests')  {
             steps{
                script  {
                    echo "Running tests..."

                    // Spin up a database service with specified env vars.
                    docker.image('mysql:latest').withEnv(['MYSQL_ROOT_PASSWORD=root', 'MYSQL_DATABASE=test']).run()

                    // Run an interactive container for the duration of test suite's execution.
                    docker.run('-e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test --rm --name test-container -v $WORKSPACE:/home/mysql/ localtest.sh'
                }
             }
         }

        // Stop and Remove Database Container
        stage('Stop and Remove Database Container')  {
            steps{
                script  {
                    echo "Stopping and removing the database container..."
                 }
             }
         }

        // Push Docker Images to Docker Hub (uncomment if needed)
        /*
        stage('Push Docker Images to Docker Hub')  {
            steps{
                script  {
                    // Push all tags of repository
                    docker.push(`$DOCKER_HUB_REPO:latest`)
                    docker.push(`$DOCKER_ HUB_REPO:stable`)
                 }
             }
         }
        */
    }

}