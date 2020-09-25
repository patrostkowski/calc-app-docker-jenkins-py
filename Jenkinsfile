pipeline {
  agent {
    docker {
      image 'python:3.8'
    }

  }
  stages {
    stage('Install') {
      steps {
        echo 'Installing libs...'
        sh 'pip3 install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        echo 'Testing app...'
        sh 'pytest -v test_calc.py'
      }
    }

  }
}