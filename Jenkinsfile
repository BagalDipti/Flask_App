
pipeline {
  environment {
        registry = "diptibagal3010"
        dockerImage = ''
        Name = "host_info"
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/BagalDipti/Flask_App.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + "/" +Name+":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '' ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Docker Run') {
        steps {
          script {
            dockerImage.run(" -p 5678:5678 --rm --name Host_Info")
          }
        }

    }

  }
}
