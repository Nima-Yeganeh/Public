pipeline {
  agent any
  
  stages {
    stage('Execute Shell Script') {
      steps {
        sh '''
          #!/bin/bash
          echo "Running shell script"
          ls -al
          echo "Done!"
        '''
      }
    }
  }
}
