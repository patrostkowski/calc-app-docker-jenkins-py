pipeline {
  }
  stages {
    stage('Build') {
      steps {
        agent {
          dockerfile {
            filename 'Dockerfile'
    }
      }
    }
    stage('Tests') {
      steps {
        echo 'Unit tests begin...'
        sh 'pytest -v'
      }
    }

    stage('Merge') {
      steps {
        echo 'Build begin'
      }
    }

  }
}