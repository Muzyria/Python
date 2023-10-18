#!/bin/sh

node convert-to-DDMM.mmmm.js

node convert-to-DDMM.mmmm-from-google-earth.js > coordinates.csv

java -jar syncwise-tcp-simulator-0.6.jar --help

java -jar syncwise-tcp-simulator-0.6.jar -env dev --request-type utilitygauge --device S10150000211018049 --limit 1
