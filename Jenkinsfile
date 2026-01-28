pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo "📥 Cloning fast-api-python repository..."
                git branch: 'main',
                    url: 'https://github.com/codeguyakash/fast-api-python.git'
            }
        }

        stage('Setup Python venv') {
            steps {
                echo "🐍 Creating virtual environment..."
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python --version
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 Installing dependencies..."
                sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Deployment Complete') {
            steps {
                echo "✅ Jenkins pipeline SUCCESS"
                echo "🚀 Next: AWS deployment later"
            }
        }
    }

    post {
        failure {
            echo "❌ Jenkins pipeline FAILED"
        }
    }
}