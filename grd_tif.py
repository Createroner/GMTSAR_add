
import os
def grd_tif(dataDir, outDir):

    # first list the .grd file
    grdFileLists = os.listdir(dataDir)

    os.makedirs(outDir,exist_ok=True)

    for i  in range(len(grdFileLists)) :

        if grdFileLists[i].endswith('.grd'):
            os.system('gdal_translate -of GTiff {}.grd {}/{}.tif'.format(dataDir + '/' + grdFileLists[i].split('.')[0],outDir,grdFileLists[i].split('.')[0]))

if __name__ == "__main__":

    import sys

    if (len(sys.argv) < 2 or len(sys.argv)> 3 ):
        print('**********************************************************************')
        print('***The preprocessing of translating .grd to .tif***')
        print('**********************************************************************')
        print('                          grd_tif   <datadir>   <outdir>              ')
        print(r'eg: grd_tif D:\GMTSAR-Processing\142-4-2020\no_gacos\sbas D:\GMTSAR-Processing\142-4-2020\no_gacos\sbas\vel')
        print('                                                                  ')
        print(' datadir  <---------->(input) intput data directory  including .grd file  ')
        print(' outdir   <---------->(input) output data directory  to create .tif file  ')
        exit()
    
    dataDir = sys.argv[1]
    outDir = sys.argv[2]
    grd_tif(dataDir, outDir)






