#!/usr/bin/bash
#This is a script used to generate a folder full of random data, with some files repeating
#
BASE_FS="/home/ateschan/Programming/Python/TAMUSA/wk2-hashing/bof"
genfile(){
  #make a handful of directories
  #for each of those directories, a random depth
  FILE_COUNT=$(($RANDOM % (14 - 1 + 1) + 1))
  mkdir ./bof
  for ((i=1; i<=$FILE_COUNT; i++))
    do
      comp=$(($i % 2));
      if [ $comp -eq 0 ]; then  
          touch "./bof$1file-$i"
          head -c 1M < /dev/urandom > "./bof$1file-$i"
          touch "./bof$1file-$i-(d)"
          cat "./bof$1file-$i" > "./bof$1file-$i-(d)"
      else
        touch "./bof$1file-$i"
        head -c 1M < /dev/urandom > "./bof$1file-$i"
      fi
    done
}

#every direcotry will call gendir and genfile once, with a random decrease in gendir chance per call

coinflip(){
  #$1 is the percent chance a directory will generate
  #$2 is the built out directory structure
  #A genfile is garunteed run
  PERCENT_CHANCE=$1
  DIR_STRUCT=$2
  DIR_COUNT=$(($RANDOM%9))

  if [ $PERCENT_CHANCE -lt 5 ]; then
    exit 0
  fi

  #$1 is the current dir
  #When called this will generate a unique and random amount of diretories within $1
  #First loop is more or less length
  for ((i=1; i<=$DIR_COUNT;i++))
  do
    mkdir -p "$BASE_FS$DIR_STRUCT/Dir-$i"
  done
  

  for ((i=1; i<=$DIR_COUNT;i++))
  do
    genfile "$DIR_STRUCT/Dir-$i/"
    coinflip $(($PERCENT_CHANCE - $((RANDOM % 7)) + 1)) "$DIR_STRUCT/Dir-$i" 
  done

}


#Number of files


#Filename
FILE=./bof/


if [ -d "$FILE" ]
  then 
  echo "$FILE exists, skipping generation"


#Generate files and fill with junk
else 
  echo "Generating a bunch o files...";
  coinflip 10000 ""
fi



echo done!
