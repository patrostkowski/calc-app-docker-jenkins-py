pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Test') {
      steps {
        sh 'pytest'
      }
    }

    stage('Finish') {
      steps {
        echo 'Tests finished'
      }
    }

  }
}