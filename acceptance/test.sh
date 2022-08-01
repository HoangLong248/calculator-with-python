#!/bin/bash

sleep 30
test $(curl --location --request GET "http://192.168.1.29:8001/sum?num1=123&num2=456") -eq 56088