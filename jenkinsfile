pipeline {
    agent any

    environment {
        // Add credentials or environment variables here if needed
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3.10 python3.10-venv python3.10-dev python3-pip
                    python3.10 -m venv venv
                    source venv/bin/activate
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Verify Pytest Installation') {
            steps {
                sh '''
                    source venv/bin/activate
                    python --version
                    which python
                    which pytest || echo "pytest NOT found"
                    python -m pytest --version || echo "pytest not working"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    python -m pytest
                '''
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    echo "Deploying the application..."
                    # Add deployment commands here
                '''
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
    }
}
