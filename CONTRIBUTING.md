# Contributing to Quindar-GMAT

This guide covers ways in which you can become a part of the ongoing development of Quindar-GMAT. Outlined in this file are:

* Reporting an Issue
* Contributing to the Quindar-GMAT code

## Code of Conduct

Quindar is committed to fostering a welcoming, collaborative and passionate community. If you encounter any unacceptable behavior, follow these steps to report the issue to the Quindar team. We are here to help. Our standards is to use welcoming and inclusive language, being respectful of differing viewpoints, accepting constructive criticism, showing empathy towards other community members, and focusing on what is best for the community. As contributors and maintainers of the Quindar, we pledge to respect everyone who contributes by posting issues, updating documentation, submitting pull requests, providing feedback in comments, and any other activities.

Communication through any of Quindar's channels (GitHub, IRC, mailing lists, Google+, Twitter, etc.) must be constructive and never resort to personal attacks, trolling, public or private harassment, insults, or other unprofessional conduct. We promise to extend courtesy and respect to everyone involved in this project regardless of gender, gender identity, sexual orientation, disability, age, race, ethnicity, religion, or level of experience. We expect anyone contributing to Quindar to do the same. If any member of the community violates this code of conduct, the maintainers of Quindar may take action, removing issues, comments, and PRs or blocking accounts as deemed appropriate.

If you are subject to or witness unacceptable behavior, or have any other concerns, please email us at quindar@quindar.space.

## Reporting an Issue
Quindar uses GitHub Issue Tracking to track issues (primarily bugs and contributions of new code). 
If you found a bug,
* Ensure that the bug was not previously reported by searching on Github under [Issues](https://github.com/quindar/quindar-gmat/issues).
* If you are unable to find an existing open issue, open a new issue. It should have a clear and descriptive title, steps to reproduce the issue, expected and actual behavior. Include code samples, screenshots wherever needed.

## Contributing to the Quindar-GMAT code

### Style Guides
We're not super strict on style guides yet, but as Quindar grows and we increasingly automate the DevOps / QA processes, consistent coding style is increasingly important. To future proof your code, please consult the following guidelines:

* [Angular v1 Guide](https://github.com/johnpapa/angular-styleguide/blob/master/a1/README.md)
* [Javascript Guide](https://google.github.io/styleguide/jsguide.html)
* [CSS+JS Guide](https://github.com/airbnb/javascript/tree/master/css-in-javascript)
* [HTML5 Guide](https://www.w3schools.com/html/html5_syntax.asp)
* [Dockerfile Guide](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)
* [Python Guide](https://www.python.org/dev/peps/pep-0008/)

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

	sudo docker exec qsrc gmat-update.sh <your feature branch>
	
Connect to the server at http://hostname or you can access the VNC server directly with a [VNC client](https://www.realvnc.com/download/viewer/) at hostname:5901 using password "vncpassword".

## To Do

* user access management integration with the quindar-proxy server
* more example scenarios
