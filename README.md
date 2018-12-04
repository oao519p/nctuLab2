# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program
> * Show the screenshot of using iPerf command in Mininet
1. First run the topology.py by " [sudo] chmod +x topology.py "
2. then can run by " [sudo] ./topology.py "
3. after running , it will enter to Mininet's CLI mode
4. use iPerf command to measure the topology 

screenshot for using iPerf command in Mininet
![](https://i.imgur.com/OUCCGq8.png)

---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail
* Mininet(topo=  , link=  , controller=  ): Create Mininet object

* addSwitch(): Add switch to topo
* addHost(): Add host to topo
* addLink(node1 , node2, bw=  , delay=  , loss=  ): node2 link with node1 (bidirectional)
---
* setLogLevel(): Setup loglevel (Convenience function to support lowercase names)
		 參數: 'info' / 'debug' / 'output'

* dumpNodeConnections(): dump connections to/from a set of nodes
* pingAll(): Ping between all hosts >> 檢測網路互通性
---
* start(): Start controller and switches
* stop(): Stop the controller(s), switches and hosts
* CLI(Mininet object): Start and run interactive or batch mode CLI
---
* TClink & OvScontroller for creating Mininet object's parameter
	

### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail

* iPerf is a tool for measuring bandwidth on IP networks
> for topo2.png , should use "h6 iperf -s -u -i 1 > ./out/result & " and "h3 iperf -c 10.0.0.6 -u -i 1"
* -s: start up with server mode
* -u: using UDP portocol
* -i 1: interval time with 1 sec
* -c 10.0.0.6: host start up with client mode (10.0.0.6 is server's address) 

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**
 * clone initial repository from github and login to container by SSH
 * run Mininet with OvS's controller ( to support topos )
> if not using OvS, it will get error .
> By solving this error, use " service openvswitch-switch start ".


2. **Example of Mininet**
 * change directory 
 * change the .py into executable mode by " chmod +x example.py "
> since the data in Mininet have no permission initial.  +x : execute
 * then see the result of creation & connection of 2 hosts and 1 switch.
![](https://i.imgur.com/tWRPUTE.png)

3. **Topology Generator**
 * view topo2.png
![](https://i.imgur.com/mYxXc9R.png)
 * generate topology.py by " touch topology.py " under /src/.
 * refer to example.py, finish topology.py 
 * code part:
> 1. create switches(numbers = 5) and hosts( = 10)
> 2. construct each links (total 14 links) and set up bandwideth, delay, loss rate
> 3. define simpleTest() and add two requirement in here
		(i) Dump every connections information
		(ii) Enter CLI mode instead of end the network immediatly


4. **Measurement**
 * change topology.py executable as task 2 done with example.py
 * execute topology.py
 * after running , it will autoly enter into Mininet CLI mode 
 * use iPerf command to test topology.py by " h6 iperf -s -u -i 1 > ./out/result & " and " h3 iperf -c 10.0.0.6 -u -i 1 "
 * it is success if loss rate is in range 13%~18%.


---
## References

> TODO: 
> * Please add your references in the following

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
    * [MININET部分指令以及其用法总结](https://wenku.baidu.com/view/c942ecb33186bceb19e8bbe8.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [吳宜珈](https://github.com/oao519p)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
