def appname = "devops"
def repo = "rm13rotem"  // Replace with your DockerHub username
def apptag = "${env.BUILD_NUMBER}"
def appimage = "docker.io/${repo}/${appname}:${apptag}"


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
              sh "docker build -t ${appimage} ."
            }
        } 
		
		stage('Docker Login') {

		    container('docker') {
		
		        withCredentials([
		            usernamePassword(
		                credentialsId: 'rm13rotem',
		                usernameVariable: 'DOCKER_USER',
		                passwordVariable: 'DOCKER_TOKEN'
		            )
		        ]) {
		
		            sh '''
		                echo "$DOCKER_TOKEN" | docker login \
		                -u "$DOCKER_USER" \
		                --password-stdin
		            '''
		        }
		    }
		}
        stage('Push Image to Docker HUB') {
            container('docker') {
              echo "push docker image..."
              sh "docker push ${appimage}"
            }
        } 

		stage('Helm template install') {
            container('docker') {
                sh '''
				
                    sudo apt update
					sudo apt install -y curl gnupg apt-transport-https
					
					curl https://baltocdn.com/helm/signing.asc | \
					gpg --dearmor | \
					sudo tee /usr/share/keyrings/helm.gpg > /dev/null
					
					echo "deb [signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | \
					sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
					
					sudo apt update
					sudo apt install -y helmhelm version
									
                    git clone https://github.com/rm13rotem/argo_gitops
                    cd argo_gitops					

                    helm template my-app ./helm > devops4.yaml

                    git add devops4.yaml
                    git commit -m "Update manifest"
                    git push
                '''
            }
        }
    }
}
