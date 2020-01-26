#!/bin/bash
touch LOGFILE
end="END"
if tail -n 1 LOGFILE | grep -q $end || [ ! -s LOGFILE ]; then #Checks if last line contains end

  if [ $1 == "start" ]; then
    echo "START " | tr -d '\n' >> LOGFILE && date >> LOGFILE
    echo "LABEL " | tr -d '\n' >> LOGFILE && echo "This is task $2" >> LOGFILE

  elif [ $1 == "status" ]; then
    echo "No task currently running"

  elif [ $1 == "log" ]; then

    arrayOfTime=( $(grep -o '[0-9][0-9]:[0-9][0-9]:[0-9][0-9]' LOGFILE) )
    arrayOfTasks=( $(grep 'task' LOGFILE | cut -d\   -f5) )
    declare -i counter=1
    for (( i=0; i<(${#arrayOfTime[@]}/2); i++ ))
    do
      time1=${arrayOfTime[(${counter}-1)]}
      time2=${arrayOfTime[$counter]}
      echo Task ${arrayOfTasks[$i]}: $(date -d @$(( $(date -d "$time2" +%s) - $(date -d "$time1" +%s) )) -u +'%H:%M:%S')
      counter+=2
    done
  else
    echo "Please use track.sh start 'name of task', track.sh stop, track.sh status, or track.sh log.
    Log will not display when a task is running. Stop only works when a task is running. Start only
    works when a task is not running."
  fi
else
  if [ $1 == "stop" ]; then
    echo "END " | tr -d '\n' >> LOGFILE && date >> LOGFILE

  elif [ $1 == "status" ]; then
    tail -n 1 LOGFILE

  elif [ $1 == "start" ]; then
    echo "A task is already running" >&2

  else
    echo "Please use track.sh start 'name of task', track.sh stop, track.sh status, or track.sh log.
    Log will not display when a task is running. Stop only works when a task is running. Start only
    works when a task is not running."
  fi
fi
