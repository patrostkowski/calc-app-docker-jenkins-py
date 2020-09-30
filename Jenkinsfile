pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Build complete. Starting tests'
      }
    }
    stage('Test') {
      steps {
        echo 'Unit tests begin...'
        sh 'pytest -v'
      }
    }

    stage('Merge') {
      steps {
        echo 'Merged to master'
      }
    }

  }
  post {
    always {
      sh './merge_branches.sh'
    }
    failure {
      echo 'something went wrong'
    }
  }
}