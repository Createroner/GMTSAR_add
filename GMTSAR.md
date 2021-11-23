---
title: GMTSAR
created: '2021-11-14T04:50:38.515Z'
modified: '2021-11-23T01:25:18.515Z'
---

# GMTSAR
关于GMTSAR有许多的步骤，在这些步骤中大致将他分成了以下几步，首先是数据准备，然后是配准

### 数据准备
一共需要准备Sentinel1数据，精轨数据，DEM数据，可以在以下网站进行下载
1. Sentinel数据
https://search.asf.alaska.edu
2. 精轨数据
https://s1qc.asf.alaska.edu/aux_poeorb/
3. DEM数据
https://topex.ucsd.edu/gmtsar/demgen/

下载好这些数据之后建立一个文件夹，这个文件夹需要包括
- data : 文件夹，用于存放下载好的Sentinel-1数据，然后cd到data目录下用unzip_sentinel-1.csh /data ， 并且把精轨数据的文件也拷到data目录下面。
- orbit : 精轨数据文件夹，将下载好的精轨hmo数据放到该文件夹下面
- topo : DEM数据文件夹，将下载好的dem.grd放到该文件夹下面
- F1 ： 这个文件是用来存放IW1第一个burst的数据的。文件夹下面需要创建raw文件夹，topo文件夹，然后cd到raw文件夹下面，现在需要做的是把IW1数据软连接到raw文件目录下面，
1. 使用./link_S1.csh  [directory]  [num] ， directory为解压后的SAR数据目录。也就是上面的data目录，num为burst的序号，选择1，2，3。对于F1则为选1。软连接了数据之后，下一步需要软连接的是DEM数据，
2. 使用命令ln -s ../../topo/dem.grd。
3. 接下来需要将精确轨道数据进行软连接link_S1_orbits.csh csh 如 ./link_S1_orbits.csh /data/orbit/
这样则完成了整个F1文件夹的准备。
- F2 ： 文件与上述相同，F2文件夹是用来存放IW2的，所以注意上述命令要改为2
- F3 ： 文件与上述相同，F3文件夹是用来存放IW3文件的，所以注意将上面的命令改成3


对于128-3选择20200128为主影像


### 配准准备
1. preproc_batch_tops.csh data.in ../topo/dem.grd 1
  这一步是数据预处理的第一步，第一个参数data.in是上面./link_s1.ch 生成的数据列表文件放在F*/raw下面，../topo/dem.grd是DEM所在的路径，1代表的是第一步，这一步将会生成baseline_table.dat和baseline.ps（这是一种格式图片）,将baseline_table.dat移动到上一层目录去，使用mv baseline_table.dat ../命令，然后可以打开baseline.ps选取主影像，选取好的主影像后，在data.in将master对应的那一行移到第一行，然后F2,F3重复这个步骤。注意：这一步可能出现can't open tiff这个时候可能是解压有问题
2. preproc_batch_tops.csh data.in ../topo/dem.grd 2
  这一步是数据预处理的第二步，这一步直接运行就可以，然后会发现在raw文件夹中生成的SLC文件比较大

3. ls *ALL*PRM > prmlist ： 这一步是存放变量
  get_baseline_table.csh prmlist S1_20200527_ALL_F1.PRM  这一步是生成新的baseline_table.data，注意每一个文件夹后面S1_20200527_ALL_F1.PRM参数不相同
  做完这几步之后，现在需要得是修改baseline_table.data, 由于原来的baseline_table.data存在一定的问题，所以这个时候需要进行修改。


### 干涉图的生成
1. tcsh /GMTSAR/gmtsar/csh/select_pairs.csh baseline_table.dat 50 100
  /GMTSAR/gmtsar/csh/select_pairs.csh baseline_table.dat 50 100
  在F1目录下（注意此时的baseline_table.dat已经更新了），用这个命令，50指的是时间基线，100指的是垂直基线的长度，在这个过程中会生成intf.in文件，这里包含了干涉对的信息
2. cp inif.in ../F2
3. cp inif.in ../F3
4. 到F2目录下，vi intf.in :%s/F1/F2/g , 然后到F3目录下vi intf.in :%s/F1/F3/g
5. cp /GMTSAR/gmtsar/csh/batch_tops.config ./ ：拷贝batch_tops.config到每个文件夹


### 在服务器上跑的实验
1. 128-3 选的主影像是20200527  S1_20200527_ALL_F1
2. 激活docker 环境sudo docker run -i -v /mnt/raidDisk/128-3/:/data -t nbearson/gmtsar /bin/bash


### 补充文档
1. D:\zlc\GMTSAR\gmtsar脚本\link_S1.csh  用于软链接Sentinel-1数据
2. D:\zlc\GMTSAR\gmtsar脚本\link_S1_orbits.csh 用于软连接精轨数据
3. D:\zlc\GMTSAR\gmtsar脚本\cor.csh 用于批处理配准脚本


### GMT画.PS文件
1. pyGMT安装 https://www.pygmt.org/dev/install.html
2. 激活conda activate pygmt
3. 将.ps文件转换为.jpg文件gmt psconvert -A baseline.ps
4. >gmt grdimage phase.grd -JX6i+ -I+d -jpg map 

### docker 命令
- sudo docker images : 查看镜像
- sudo docker ps : 查看正在运行的container
- sudo docker ps -a : 查看所有的container
- sudo docker stop $(docker ps -q) & docker rm $(docker ps -aq) : 停用并删除所有的容器
- sudo docker stop ID : ID为关闭容器的ID
- sudo docker rm ID : ID为删除容器的ID
- systemctl status docker : 查看docker 运行情况
- systemctl start docker ： 启动docker
- systemctl stop docker : 关闭docker
- apt-get update  : 先更新再安装
- apt-get install sudo ： linux 安装sudo
- apt-get install vim : 安装vim
- docker rmi ： docker 删除images
- sudo docker exec -i -t 1238f6e5c82f /bin/bash : 进已经run的环境


### bash 命令
1. bash select_pairs.sh baseline_table.dat 50 100

###  tcsh
1. 以后所有的gmtsar都在tcsh上面运行


### inif.csh需要用上
1. cleanup.csh
2. dem2topo_ra.csh


### 自己写的东西
1. ls -d disp_* > dislist  ， 把此文件夹里面包含disp地全部放到dislist 里面去
2. 当出现permisission denied : chmod 777 /usr/local/GMTSAR/bin/unzip_sentinel-1.csh 


### ALOS实验
1. 选取的主影像为IMG-HH-ALOS2251300700-190117-FBDR1.1__A
2. http://gmt.soest.hawaii.edu/boards/6/topics/6265 参考的这篇文献
3. 运行命令p2p_processing.csh ALOS2 IMG-HH-ALOS2011986990-140813-HBQR1.1__A IMG-HH-ALOS2014056990-140827-HBQR1.1__A config.ALOS2.txt
4. 已经完成190117-190228 ，190117-190523
5. p2p_processing.csh ALOS2 IMG-HH-ALOS2251300700-190117-FBDR1.1__A IMG-HH-ALOS2257510700-190228-FBDR1.1__A config.ALOS2.txt   （这个命令是190117-190228） 已经完成
6. p2p_processing.csh ALOS2 IMG-HH-ALOS2251300700-190117-FBDR1.1__A IMG-HH-ALOS2269930700-190523-FBDR1.1__A config.ALOS2.txt   （这个命令是190117-190523） 正在进行
7. p2p_processing.csh ALOS2 IMG-HH-ALOS2251300700-190117-FBDR1.1__A IMG-HH-ALOS2278210700-190718-FBDR1.1__A config.ALOS2.txt   （这个命令是190117-190523） 待命

### 命令总结
1. 到data文件夹 unzip_sentinel-1.csh /data/panzhihua-26-11  11/23/20：00  ~ 11/23/22：00 ， 花了两个小时
2. cd ../F1; mkdir raw; cd raw; link_S1.csh ../../data/ 1; link_S1_orbits.csh ../../orbit/; ln -s ../../topo/dem.grd
3. cd ../../F2; mkdir raw; cd raw; link_S1.csh ../../data/ 2; link_S1_orbits.csh ../../orbit/; ln -s ../../topo/dem.grd
4. cd ../../F3; mkdir raw; cd raw; link_S1.csh ../../data/ 3; link_S1_orbits.csh ../../orbit/; ln -s ../../topo/dem.grd
5. cd ../../F1/raw; preproc_batch_tops.csh data.in dem.grd 1; mv baseline_table.dat ../ ; 接下来修改data.in，把master放在第一个s1a-iw1-slc-vv-20180811t111556;  preproc_batch_tops.csh data.in dem.grd 2

