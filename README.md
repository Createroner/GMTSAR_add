# ReadMe
###  batch_geocode.py ： 是用来批处理地理编码的
1. 在服务器sbas/目录下面 batch_geocode.py trans.dat ./ ./geocoding
2. 最终将会在geocoding目录下面生成所有的地理编码之后的结果
### grd_tif.py ： 是批量把grd格式转成tif格式的
1. 在Windows下面打开prompt; activate pygmt
2. F:; cd  F:\GMTSAR\myscript; 
3. python F:\GMTSAR\myscript\grd_tif.py D:\GMTSAR-Processing\142-4-2020\no_gacos\sbas D:\GMTSAR-Processing\142-4-2020\no_gacos\sbas\vel
4. 最终将会在vel目录下面生成最终所有的tif
### cp_png.csh : 这个文件是将在merge目录下面，将一系列的图进行复制到一个统一的文件夹下面
1. cp_png.csh unwrap.pdf unwrap ： 第一个参数是需要拷贝的文件的名称，第二个参数是目标目录
