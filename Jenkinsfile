pipeline {
  agent {
    docker {
      image 'python:3.8'
    }

  }
  stages {
    stage('Install') {
      steps {
<<<<<<< HEAD
        sh '''
	pytest
	exit $?
	'''
=======
        echo 'Installing libs...'
        sh 'pip3 install -r requirements.txt'
>>>>>>> cabd5024ee576b476acf0634d02fea843137b2e0
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
