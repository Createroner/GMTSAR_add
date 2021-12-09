#!/bin/tcsh -f
# Lichuan Zou, 2021/12/8
# .csh unwrap.pdf unwrap/
# unwrap is the cp file name
# unwrap/ is the destinational file 

set name = $1

set out_dir = $2

rm -rf dirlist.in

ls -d 20* > dirlist.in

set dir_list = `cat dirlist.in`

foreach line($dir_list) 

    echo $line 

    cp $line'/'$1 $2/$line'_'$1
    
end
