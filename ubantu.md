---
title: ubantu
created: '2021-08-16T01:58:30.906Z'
modified: '2021-11-23T01:39:09.388Z'
---

# ubantu
- 添加临时环境变量
`export PATH=/mnt/hgfs/zlc/software/SNAPHU/snaphu-v1.4.2_linux/bin:$PATH`
-打开当前cmd下面的文件夹
`nautilus`
- ubantu 获得root权限
1. sudo passwd root
2. su root
3. sudo su
4. cd .. 是返回上一层目录

- ubantu 删除文件夹
1. sudo rm -r 文件夹名

### vs2019 下面的git管理
1. 首先进行git->提取
2. 再全部提交
3. 再推送


- 启动matlab sudo /usr/local/MATLAB/R2018a/bin/matlab
- ubantu 安装matlab 参考https://www.cnblogs.com/iwuqing/p/9833292.html文章

### 怎么在ubantu里面装matlab
具体过程参考https://www.cnblogs.com/iwuqing/p/9833292.html
1. 首先需要下载matlab文件，包含三个文件Matlab 2018a Linux64 Crack.tar.gz 、 R2018a_glnxa64_dvd1.iso、 R2018a_glnxa64_dvd2.iso
2. 开始在uabtnu 里面挂载镜像 挂载dvd1：sudo mount -t auto -o loop ./Linux/R2018a_glnxa64_dvd1.iso ./matlab/ 其中./matlab/是指挂在到的文件夹
3. 然后开始安装sudo ./matlab/install ，在安装过程中可以根据需要进行包的选择。
4. 如果有的工具安装过程中需要挂载第二个镜像，则像上一步重新打开一个cmd把它也挂在到matlab文件夹下面


### 在VM下安装VM tools
1. https://blog.csdn.net/Lcking18325/article/details/103249783

### ubantu安装anaconda
1. 下载anaconda https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
2. https://blog.csdn.net/haeasringnar/article/details/82079943

-https://blog.csdn.net/jinking01/article/details/82490688 ： ubantu下面装docker


- ubantu 删除软连接：rm -rf 映射目录
- ubantu 增加软连接：ln -s 需要增加的
- ubantu 查看当前软连接： ls -il

- 查看当前镜像 docker images
- 查看当前所有容器 docker ps -a
- 查看当前运行的容器 docker ps
- 开始当前容器 docker start 当前容器名

- 改变当前shell 是bash 还是 csh https://blog.csdn.net/weixin_45386875/article/details/116231811

- vim 显示行数set number

- docker run -i -t nbearson/gmtsar /bin/bash 生成一个实例

- docker 挂在设备 https://www.cnblogs.com/djlsunshine/p/11284463.html#:~:text=docker%E6%9C%AC%E8%BA%AB,ount%E7%9A%84%E6%9C%BA%E5%88%B6%E3%80%82

- 挂在实例docker run -i -v /G/ISCE/128-3:/data -t nbearson/gmtsar /bin/bash

- 注意对于GMTSAR选的参考点不同，最后出来的点的数量也不一样

### centors
1. 在centors 上运行yum任何操作的时候先sudo
2. 要使用docker的时候，先sudo service docker start 
3. 然后查看是否安装成功的时候，sudo docker images
4. https://blog.csdn.net/vivian187/article/details/51476043 ubantu查看cpu运行情况


