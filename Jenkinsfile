
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/Python']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '39e50685-68eb-41f5-9575-dfb7ee803e99', url: 'https://github.com/prathamesh077/Python_Projects.git']]])
				
            }
        }
		stage('Build'){
			steps{
				git branch: 'Python', credentialsId: '39e50685-68eb-41f5-9575-dfb7ee803e99', url: 'https://github.com/prathamesh077/Python_Projects.git'
				bat 'Python Hello.py'
			}
		}
		stage('Test'){
			steps{
				echo "This job is under testing...."
				git branch: 'Python', credentialsId: '39e50685-68eb-41f5-9575-dfb7ee803e99', url: 'https://github.com/prathamesh077/Python_Projects.git'
				bat 'Python Match-case.py'
			}
		}
    }
}
 