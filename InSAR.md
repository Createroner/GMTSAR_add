---
attachments: [Clipboard_2021-11-08-22-07-23.png, Clipboard_2021-11-08-22-07-31.png]
title: InSAR
created: '2021-08-16T02:03:50.709Z'
modified: '2021-11-15T12:02:28.993Z'
---

# InSAR
- 使用SNAP进行InSAR处理，到unwrapp这一个步骤
1. Split : Radar->Sentinel-1 TOPS -> S-1 TOPS split , 这一步的目的是选择IW1,IW2,IW3三个条带中的一个，并且选择极化方式等，做InSAR选择SLC模式，IW模式，VV极化
2. Apply Orbit : Radar -> Apply Orbit file , 注意在这一步选择Processing Parameters 中Do net fail.... 这一步的目的是为了添加精轨数据
3. 注意在coregistration之前需要确定一个主影像: Radar -> Interfermtric -> InSAR StackOverview.
3. coregistration ：Radar -> Coregistration -> S1 TOPS Corgistraation -> S-1 Back Geocoding 。 这一步的目的是为了将干涉需要的两幅图进行配准，方便后面进行共轭相乘，得到相位图，并且方便对子区域进行裁剪。
4. Deburst ： Sentinel-1 TOPS -> S1 TOPS Deburst 。 这一步的目的是为了可以发现前面的图像有间隔的条带，这一步的目的就是为了把这个条带给去掉
5. Create subset ： 这一步是在图像中进行，选择需要裁剪的区域（这一步一般用鼠标和滚轮进行完成），然后右键Spatial Subset from View..这一步的目的是为了裁剪出小的区域然后方便后面的计算，可以减少后面解缠相位所花的时间
6. Generate Interferogram ：Radar -> Interferometric -> Products -> Interferogram Formation 。 这一步则是得到干涉图
7. Phase Unwarpping ： Radar -> Interferometric -> Unwrapping -> Snaphu Export 将导出的文件下找到snaphu.conf文件，然后执行里面的命令，然后在Ubantu系统上进行解缠。解缠完毕以后，选择import在第二个参数里面选择解缠完毕的如（UnwPhase_ifg_IW1_VV_24Mar2017_05Apr2017.snaphu.img）文件
8. Gecoding : Radar-> Geometric -> Terrin Correction -> Range-Doppler Terrain Correction : 这一步主要进行的是地理编码，得到的图最后可以叠加到Goodle Earth上面去看结果。
9. 导出STRAMP格式的是时候，需要也把subset这个文件夹也放进去和干涉图文件夹，需要这两个文件夹



-https://asf.alaska.edu/how-to/data-recipes/phase-unwrap-an-interferogram/ ： 利用SNAP做InSAR的整个过程


### 在ubantu系统上安装staMPS
- 主要参考https://forum.step.esa.int/t/stamps-4-1-beta-installation-in-ubuntu-18-04/21045/7
1. 下载staMPS压缩包 https://github.com/dbekaert/StaMPS
2. 解压下载完成的压缩包 unzip ---
3. 进入src文件夹
4. make
5. make install 
6. 在StaMPS_CONFIG.bash和StaMPS_CONFIG.tcsh下修改全局变量
7. 如export STAMPS="/home/zlc/Documents/StaMPS-4.1-beta"与snap变量的路径
8. bash
9. source StaMPS_CONFIG.bash
10. tcsh
11. source StaMPS_CONFIG.tcsh
12. 测试是否安装完成mt_prep_snap命令，出现提示则说明完成

### Envi 进行tif图的拼接
1. Mosaicking -> Seamless Mosaic

### StamPS的操作步骤
1. 在ubantu上打开matlab , 点击set path 把StamPS-4.1-beat 里面matlab的两个路径加载进去
2. 在StamPS-4.1-beat文件夹里面打开cmd , bash ->  source StaMPS_CONFIG.bash -> tcsh -> source StaMPS_CONFIG.tcsh
3. 准备好环境后，现在cmd到SNAP导出的STMAP格式的数据下面，mt_prep_snap 20180114 /home/ubuntu-18043-psinsar/Desktop/test/INSAR_20180114 0.4 3 2 50 200 . 第二个参数是时间，第二个是导出数据文件加，0.4是选PS的严格性
4. 准备好后，现在把matlab的路径导到上面数据准备的文件夹下面，分别执行stamps(1,1) - > stamps(7,7)

### Stamps 代码意思
1. getparm : 可以查看整个stamps的参数设置
2. setparm('变量', 值) ： 这一步是对变量进行修改
3. stamps(1,1) : 对数据进行导入
4. stamps(2,2) : 估计相位的噪音
5. stamps(3,3) : 选择PS点
6. stamps(4,4) : 去除多余的PS点（比如强散射是由于周围的点引起的）
6. stamps(5,5) : 去相关
7. stamps(6,6) : 相位解缠

### GACOS
1. 下载好的S1文件是UTC时间

### 高性能InSAR
1. xiangganmubiao 用byte
2. xiangganxishu 用float
3. 在xiangganmubiao 和 xiangganxishu上找参考点，要大的点
4.  20200104-20200209可能存在问题

### ISCE
1. Anaconda 安装ISCE https://zhuanlan.zhihu.com/p/269183148

### 处理攀枝花数据
1. 数据存在V:\26-11


























