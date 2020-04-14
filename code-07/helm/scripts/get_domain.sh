#!/bin/bash

NS=$1

INGRESS_IP=`kubectl get svc -n $NS traefik-public -o jsonpath='{.status.loadBalancer.ingress[*].ip}' 2> /dev/null`
exit_status=$?
if [ $exit_status -eq 0 ]; then
  if [ $INGRESS_IP ]; then
    INGRESS_IP="$INGRESS_IP.xip.io"
  else
    INGRESS_IP=''
  fi
else
  INGRESS_IP=''
fi

echo $INGRESS_IP
