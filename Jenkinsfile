def appname = "devops_4"
def repo = "rm13rotem"  // Replace with your DockerHub username
def appimage = "docker.io/${repo}/${appname}"
def apptag = "${env.BUILD_NUMBER}"

podTemplate(cloud: 'kubernetes', containers: [
    containerTemplate(
        name: 'jnlp', 
        image: 'jenkins/inbound-agent:latest'
    ),
     containerTemplate(
        name: 'docker', 
        image: 'docker:26-dind', // Use the latest stable DinD image
        privileged: true,      // Essential for Docker daemon to run
        args: '--storage-driver=vfs' // VFS is safest for K8s, though slower
    )], 
  volumes: [
    emptyDirVolume(mountPath: '/var/lib/docker', memory: false) // Q: Why do we need this volume?
  ]) {
    node(POD_LABEL) {
        stage('Checkout from git') {
            container('jnlp') {
            sh '/usr/bin/git config --global http.sslVerify false'
	    checkout scm
          }
        } 

        stage('Build Image') {
            container('docker') {
              echo "Building docker image..."
              sh "docker build -t $(appimage):1.$(apptag} ."
            }
        } 
		
        stage('Push Image to Docker HUB') {
            container('docker') {
              echo "push docker image..."
              sh "docker push $(appimage):1.${apptag}"
            }
        } 
    }
}
