#!/bin/bash
#  script that displays the size of the body of the response
curl -s 0.0.0.0:5000 | wc -c
