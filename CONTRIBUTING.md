#Contributing to Quindar-GMAT

This guide covers ways in which you can become a part of the ongoing development of Quindar-GMAT.

Outlined in this file are:
* Reporting an Issue
* Contributing to the Quindar-GMAT code

## Reporting an Issue
Quindar uses GitHub Issue Tracking to track issues (primarily bugs and contributions of new code). 
If you found a bug,
* Ensure that the bug was not previously reported by searching on Github under [Issues](https://github.com/quindar/quindar-gmat/issues).
* If you are unable to find an existing open issue, open a new issue. It should have a clear and descriptive title, steps to reproduce the issue, expected and actual behavior. Include code samples, screenshots wherever needed.

## Contributing to the Quindar-GMAT code
### Scenarios
* You can contribute by creating new scenario files.  Your script files need to be placed in /application/userfunctions/python/ to use the existing python functions.
* Check NASA's [User Guide](http://gmat.sourceforge.net/docs/R2016a/html/index.html) for more information about script files.

### Python functions
* You can contribute by creating new python functions that can be used by Quindar-GMAT.  Your python functions need to be placed in /application/userfunctions/python/.

### GMAT
* You can contribute by modifying Quindar-GMAT.  Check NASA's [GMAT Wiki](http://gmatcentral.org) to learn more about GMAT.

### Clone the repositories
There are two repositories needed to deploy the Quindar-GMAT project locally. 
* Quindar-deploy
* Quindar-gmat

Clone the two repositories in a single folder, such as ~/repositories

    cd ~
    mkdir repositories
    cd repositories
    git clone https://github.com/quindar/quindar-deploy.git
    git clone https://github.com/quindar/quindar-gmat.git

### Build and Run Docker container for Quindar-GMAT

	cd quindar-deploy/qsrc-simulator
	docker build -t "quindar-qsrc" .
	docker run -d -t --name qsrc --cap-add SYS_PTRACE -v /proc:/host/proc:ro -p 80:80 -p 443:443 -p 5901:5901 quindar-qsrc
	
By default, quindar-qsrc will be connected to quindar-gmat repository in GitHub.  To run your version of quindar-gmat, you need to creat your own [feature branch](https://github.com/quindar/quindar-ux/tree/master) and run the following command.

	sudo docker exec qsrc gmat-update.sh <branch>
	
Connect to the server at http://hostname or you can access the VNC server directly with a [VNC client](https://www.realvnc.com/download/viewer/) at hostname:5901 using password "vncpassword".