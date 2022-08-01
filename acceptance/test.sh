#!/bin/bash

sleep 60
test $(curl --location --request GET "calculator:8001/sum?num1=123&num2=456") -eq 56088