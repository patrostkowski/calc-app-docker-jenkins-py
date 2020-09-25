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
        sh '''pip3 install numpy:1.19.2
pip3 install pytest:6.0.2'''
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