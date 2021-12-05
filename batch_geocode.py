import os

def batch_geocode(datDir, outDir):
    
    os.system("rm -rf {}".format(outDir))

    os.system("mkdir {}".format(outDir))

    #os.makedirs(outDir, exist_ok=True)

    grdFileList = os.listdir(dataDir)

    for i in range(len(grdFileList)):

        if grdFileList[i].endswith('.grd') and "disp" in grdFileList[i]:
            
            os.system("proj_ra2ll.csh trans.dat {}.grd {}/{}_ll.grd".format(grdFileList[i].split('.')[0],outDir,grdFileList[i].split('.')[0]))
            #print(grdFileList[i])


if __name__ == "__main__":

    import sys

    if (len(sys.argv) < 3 or len(sys.argv)> 4 ):
        print('**********************************************************************')
        print('***The preprocessing of geocoding batch of grd file***')
        print('**********************************************************************')
        print('                          batch_geocode   <datadir>   <outdir>              ')
        print(r'eg: batch_geocode.py trans.dat ./ ./geocoding')
        print('                                                                  ')
        print(' trans.dat  <----------> This is including gecodeing parameters ')
        print(' datadir  <---------->(input) intput data directory  including .grd file  ')
        print(' outdir   <---------->(input) output data directory  to  create geocoded .grd file  ')
        exit()
    
    dataDir = sys.argv[2]
    outDir = sys.argv[3]
    batch_geocode(dataDir, outDir)
