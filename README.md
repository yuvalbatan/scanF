<p align="center">

<img src="https://user-images.githubusercontent.com/114166939/195892047-1e772570-14d0-4a01-aa23-256e02b48337.png">
</p>

### Introduction
ScanF is a port scanner which using Multithreading for extra speed.
This tool have 3 different options of scanning, by necessity.
It will show the user open ports on the target ip very quickly.
This tool is user friendly and very easy to use.

### Features
* -w - scan Well Known ports. (fast scan)

![image](https://user-images.githubusercontent.com/114166939/195919843-fd42134a-f17d-4d59-91a0-f447a22d9472.png)

* -r - scan ports on selected range.

![image](https://user-images.githubusercontent.com/114166939/195920277-cf0b849d-c1a3-4c27-86ad-3cb4922f650e.png)


* -a - scan all ports - 1 to 65,535. (this method is slower)
 
![image](https://user-images.githubusercontent.com/114166939/195920633-3b50f296-4525-4e93-a605-87307304c178.png)

### Python libraries
* socket.
* threading.

### How To Use
* Clone the repository to your computer.
  Guide: https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository?platform=linux
* Enter to the location of the repository.
* For Linux users - give a premission to run by using the command: "sudo chmod +x scanf.py".
* Run the tool by using the command: "sudo python3 scanf.py".
![image](https://user-images.githubusercontent.com/114166939/195914876-ea568ac3-8da6-434d-9842-84b8452d33b2.png)
* Enter the target ip and choose the option.

*** The tool built for studying and CTF purposes only! 
