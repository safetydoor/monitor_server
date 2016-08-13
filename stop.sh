#!/bin/sh

PROCESS=`ps -ef|grep monitor|grep -v grep|grep -v PPID|awk '{ print $2}'`
for i in $PROCESS
do
  echo "Kill process [ $i ]"
  kill -9 $i
done
