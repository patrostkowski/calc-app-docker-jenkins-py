pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Test') {
      steps {
        sh '''pytest
exit $?'''
      }
    }

    stage('Finish') {
      steps {
        echo 'Tests finished'
      }
    }

  }
}