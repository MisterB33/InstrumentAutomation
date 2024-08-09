#Majid Reza Barghi 
#August 6th 2024 
#Multi Diag Test for the purpose of running a unit test multiple times and loging all fails in a FAIL-logFile
#Multi Diag Test for the purpose of running a unit test multiple times and login
g all fails in a FAIL-logFile

#!/bin/bash
#capturing the start time of the test
begin=$SECONDS

#Initial Pass Counter
counter=0

#inline variables ======> TotalRuns TestDiagToRun NameofTest NameofLog #ofPassIt
emsPerUnitTest

total=$1
name="${3}"
logName=$4
testDiag=$2
PassCondition=$6
FailCondition=$7


declare -i passitems=$5
declare -i counter2

declare -i totalfail=0
rm $logName
echo "=====================================";
echo "Begining High Run ${name} Test"
echo "=====================================";
for i in $(seq $1);
do
        ./$testDiag --all | tee results.txt
        counter2=$((`grep -o "${PassCondition}" results.txt |  wc -l`))
        failcounter=$((`grep -o "${FailCondition}" results.txt | wc -l` ))
        if [ $failcounter -gt 1 ]; then
                echo "=====================================">>FAIL-$logName
                echo "FAILED AT ROUND ${i}" >> FAIL-$logName
                echo "=====================================">>FAIL-$logName
                cat results.txt >> FAIL-$logName
        fi

        if [ $counter2 -eq $passitems ]; then
                ((counter+=1))
        fi
        echo "=====================================";
        echo "${name} Test Passed Count: ${counter}";
        echo "=====================================";
        totalfail=totalfail+failcounter
        rm results.txt

done
#Calculate the time it took for test to run and store it in duration
duration=$((SECONDS - begin))
#Calculate Pass rate, needs to be in perecentage
passRate=$((counter/total))
echo "=====================================" >> $logName
echo "${name} Test Result Summary: ${counter}" >> $logName
echo "=====================================" >> $logName
echo "Total Test Runs : ${total} " >> $logName
echo "Total Test Passed : ${counter}">> $logName
echo "Total Test Failed : ${totalfail}">> $logName
echo "Pass Rate: ${passRate}" >> $logName
echo "Test Duration: ${duration} Seconds" >> $logName
head -10 $logName