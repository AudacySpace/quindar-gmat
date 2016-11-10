# quindar-gmat
Updated: Jul 18, 2016 by Ray Lai, Masaki Kakoi

The GMAT orbit trajectory simulation can be used to generate telemetry data for Quindar or for orbit simulation independent of any software. This build uses Docker for containerization and adds integration with REST API, RabbitMQ and webSockets using Python.

## Step-by-step quide to build General Mission Analysis Tool: Linux version
1. Login to the server and go to the directory where you want to build GMAT
1. Download GMAT-src-R2015a-Mac-Linux-Bug-Fixes.tar.gz by typing the following commands:
  * sudo wget "https://sourceforge.net/projects/gmat/files/GMAT/GMAT-R2015a/GMAT-src-R2015a-Mac-Linux-Bug-Fixes.tar.gz"
1. Download GMAT-datafiles-R2015a.zip:
  * sudo wget "https://sourceforge.net/projects/gmat/files/GMAT/GMAT-R2015a/GMAT-datafiles-R2015a.zip"
1. Unzip both folders:
  * sudo tar -xvzf GMAT-src-R2015a-Mac-Linux-Bug-Fixes.tar.gz
    - This creates a folder GMAT-R2015a.
  * sudo unzip GMAT-datafiles-R2015a.zip
    - This creates a folder GMAT-datafiles-R2015a.
1. Install necessary software packages:
  * sudo yum groupinstall "Development Tools"
  * sudo yum install csh
  * sudo yum install gtk3-devel
  * sudo yum install freeglut-devel
  * sudo yum install python34
  * sudo yum install python34-devel
  * sudo yum install cmake
1. Build dependencies:
  * Go to depends folder under GMAT-R2015a
  * Check if configure.sh is executable:
    - ls -al
  * If the file is not executable, change it to executable:
    - sudo chmod ugo+x configure.sh
  * Change line 159, from WX_$wx_version_download.tar.gz to v$wx_version.tar.gz
    - sudo vim configure.sh to open the file using vim
	- Type :159 to go to line 159
	- Press i to change to the insert mode
	- Change WX_$wx_version_download.tar.gz to v$wx_version.tar.gz
	- Press Esc to exit the insert mode
	- Type :w to save
	- Type :q to exit vim
  * Execute the file:
    - sudo ./configure.sh
1. Run cmake
  * Change directory to GMAT-R2015a:
    - cd ..
  * Run cmake with CMakeLists.txt
    - sudo cmake CMakeLists.txt
1. Correct errors:
  * CMake fails to include dependency directory depends/cspice/linux/cspice64/include.
    - cp depends/cspice/linux/cspice64/include/* src/base/util/ #copy the dependencies into the folder of the files which depend on them.
  * Make expects depends/cspice/linux/cspice64/lib/cspice.a, but file is named cspiced.a
    - cp depends/cspice/linux/cspice64/lib/cspiced.a depends/cspice/linux/cspice64/lib/cspice.a #makes a copy of cspiced.a named cspice.a
1. Build GMAT:
  * sudo make
1. Move the data folder under application folder:
  * Go to GMAT-datafiles-R2015a
  * Copy the data folder under application folder:
    - e.g. sudo cp -a data ../GMAT-R2015a/application/data
1. Run GMAT
  * Move to application/bin folder:
  * Test if GMAT runs:
  * e.g. sudo ./GmatConsole ../samples/Ex_Attitude_VNB.script
  
## Step-by-step quide to connect Python to General Mission Analysis Tool: Linux version
1. Find where Python.h is located:
  * find / -name Python.h
1. Open CMakeCache.txt.  This file is located in the same directory as CMakeList.txt under GMAT_R2015a.
  * sudo vim CMakeCache.txt
1. Edit two lines to specify the location of Python.h and Python library: e.g.,
  * Type :310 to go to line 310
    - Press i to change into the insert mode
	- PYTHON_INCLUDE_DIR:PATH=/usr/include/python3.4m
	- Press Esc, type :w to save
  * Type :313 to go to line 313
    - Press i to change into the insert mode
	- PYTHON_LIB_DIR:PATH=/usr/bin/python3.4
	- Press Esc, type :w to save, type :q to exit vim
1. Run cmake:
  * sudo cmake CMakeLists.txt
1. Build GMAT
  * sudo make
1. After GMAT is successfully build, GMAT should be able to call Python functions: e.g.,
  * From GMAT-R2015a, go into application/userfunctions/python
  * Download necessary files: git clone https://github.com/audacyDevOps/quindar-gmat.git
  * Copy files from quindar-gmat to python: sudo cp -r quindar-gmat/* .
  * Go to /application/bin and type ./GMAT to open GMAT.
  * Open DataGeneration.script from /application/userfunctions/python
  * Run GMAT by clicking the run button.