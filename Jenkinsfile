pipeline {
    agent any

    environment {
        SERVER_IP = credentials('aws-ec2-ip')
        APP_DIR   = credentials('aws-ec2-app-dir')
        PM2_APP   = credentials('aws-ec2-pm2-app')
    }

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

        stage('Deploy to AWS EC2') {
            steps {
                echo "🚀 Deploying to AWS EC2..."

                sshagent(['aws-ec2-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${SERVER_IP} '
                        cd ${APP_DIR} &&
                        git pull origin main &&
                        source venv/bin/activate &&
                        pip install -r requirements.txt &&
                        pm2 restart ${PM2_APP}
                    '
                    """
                }
            }
        }
    }

    post {
        success {
            emailext(
                subject: "✅ FastAPI Deployment SUCCESS on AWS EC2 ",
                body: """
                    Deployment Successful 🚀

                    Job Name: ${env.JOB_NAME}
                    Build Number: ${env.BUILD_NUMBER}
                    Build URL: ${env.BUILD_URL}
                    Build Time: ${env.BUILD_TIME}
                    Build Date: ${env.BUILD_DATE}
                    Build Version: ${env.BUILD_VERSION}
                    Build User: ${env.BUILD_USER}
                    Build Agent: ${env.BUILD_AGENT}
                    Build Agent Name: ${env.BUILD_AGENT_NAME}
                    Build Agent Version: ${env.BUILD_AGENT_VERSION}
                    Build Agent OS: ${env.BUILD_AGENT_OS}
                    Build Agent Architecture: ${env.BUILD_AGENT_ARCHITECTURE}
                    Build Timestamp: ${env.BUILD_TIMESTAMP}
                    Build Workspace: ${env.BUILD_WORKSPACE}

                    Server: AWS EC2
                    App: FastAPI
                    Status: SUCCESS
                    """,
                to: "codeguyakash.dev@gmail.com"
            )
            echo "✅ Deployment Successful"
        }
        failure {
            emailext(
                subject: "❌ FastAPI Deployment FAILED on ${env.BUILD_NUMBER}",
                body: """
                    Deployment Failed ❌

                    Job Name: ${env.JOB_NAME}
                    Build Number: ${env.BUILD_NUMBER}
                    Build URL: ${env.BUILD_URL}
                    Build Time: ${env.BUILD_TIME}
                    Build Date: ${env.BUILD_DATE}
                    Build Version: ${env.BUILD_VERSION}
                    Build User: ${env.BUILD_USER}
                    Build Agent: ${env.BUILD_AGENT}
                    Build Agent Name: ${env.BUILD_AGENT_NAME}
                    Build Agent Version: ${env.BUILD_AGENT_VERSION}
                    Build Agent OS: ${env.BUILD_AGENT_OS}
                    Build Agent Architecture: ${env.BUILD_AGENT_ARCHITECTURE}
                    Build Timestamp: ${env.BUILD_TIMESTAMP}
                    Build Workspace: ${env.BUILD_WORKSPACE}

                    Please check Jenkins logs immediately.
                    """,
                to: "codeguyakash.dev@gmail.com"
            )
            echo "❌ Deployment Failed"
        }
    }
}