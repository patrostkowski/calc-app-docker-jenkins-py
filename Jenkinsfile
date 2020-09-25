pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Tests') {
      steps {
        echo 'Unit tests begin...'
        sh 'pytest -v test_calc.py'
      }
    }

    stage('Finished') {
      steps {
        echo 'Finished'
      }
    }

  }
}