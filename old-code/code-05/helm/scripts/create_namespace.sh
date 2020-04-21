#!/bin/bash

NS=$1
 
kubectl get namespace $NS 2> /dev/null
exit_status=$?

if [ $exit_status -eq 0 ]; then
  echo "Namespace $NS Already exists"
else
  echo "Missing Namespace $NS creating now"
  kubectl create namespace $NS
fi
