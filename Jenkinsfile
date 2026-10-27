

pipeline {
    agent any

    environment {
        DOCKER_HOST = 'tcp://docker-dind:2375'
        IMAGE_NAME = 'aws-devops-flask'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Sahilpaul07/aws-devops-cicd-project.git'
            }
        }

        stage('Check Files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'git --version'
            }
        }

        stage('Docker Connection') {
            steps {
                sh 'docker info'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Automated Tests') {
    steps {
        sh 'docker run --rm -e PYTHONPATH=/app --entrypoint python ${IMAGE_NAME}:${IMAGE_TAG} -m unittest discover -s /tests -p "test*.py" -v'
    }
}
