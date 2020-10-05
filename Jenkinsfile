pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Building app'
	sh 'python -m py_compile /code/calc.py'
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
}
