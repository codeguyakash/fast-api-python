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

        stage('Check Python') {
            steps {
                echo "🐍 Checking Python version..."
                sh '''
                    python3 --version || python --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 Installing dependencies from requirements.txt..."
                sh '''
                    pip3 install -r requirements.txt || pip install -r requirements.txt
                '''
            }
        }

        stage('Deployment Complete') {
            steps {
                echo "✅ Code successfully deployed on Jenkins server"
                echo "🚀 Next step: AWS deployment will be added later"
            }
        }
    }

    post {
        success {
            echo "🎉 Jenkins pipeline SUCCESS"
        }
        failure {
            echo "❌ Jenkins pipeline FAILED"
        }
    }
}