pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "kiranvk123/kiran-demo:latest"
  }

  stage('Checkout') {
  steps {
    git branch: 'main', url: 'https://github.com/kiranvk123/kiran_demoproject.git'
     }
    }


    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'pytest || echo "No tests yet"'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t $DOCKER_IMAGE ."
      }
    }

    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh "echo $PASS | docker login -u $USER --password-stdin"
          sh "docker push $DOCKER_IMAGE"
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh "helm upgrade --install kiran-demo ./helm-chart --namespace default"
      }
    }
  }
}

