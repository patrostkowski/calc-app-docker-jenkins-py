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
        sh 'pytest -v'
      }
    }

    stage('Build') {
      steps {
        sh '''mkdir calc && 
pyinstaller --onefile /code/calc.py &&
ls -la calc/ls'''
      }
    }

  }
}