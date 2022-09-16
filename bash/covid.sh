#!/bin/bash
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
VENTILATOR=$(echo $DATA | jq '.[0].onVentilatorCurrently')
ICU=$(echo $DATA | jq '.[0].inIcuCurrently')
DEATHINCREASE=$(echo $DATA | jq '.[0].deathIncrease')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases and $NEGATIVE negative COVID tests. There are $VENTILATOR patients on ventilators currently and $ICU in the ICU. The death increase is $DEATHINCREASE." 

