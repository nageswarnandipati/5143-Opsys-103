# CPU SHEDULING 

## Teammates:
### Athul sajikumar
### nageshwar nandipatti
### sai koushik patibanda
## These are the results of some testings that we did on different algorithms and there comparisons and observations:

## python3 sim.py sched=FCFS cpus=10 ios=5 input=small_cpu.dat
CPU Utilization: 83.7620578778135                                                                                                                      IO Utilization: 13.954983922829582                                                                                                                     Average Turnaround Time: 282.2                                                                                                                         Average Wait Time: 0.0                                                                                                                                 Average I/O Wait Time: 0.0 


## python3 sim.py sched=FCFS cpus=10 ios=10 input=small_io.dat
### CPU Utilization: 36.5650406504065                                                                                                                  ### IO Utilization: 46.5650406504065                                                                                                                   ### Average Turnaround Time: 409.0                                                                                                                     ### Average Wait Time: 0.0                                                                                                                             ### I/O Wait Time: 0.0

## python3 sim.py sched=FCFS cpus=10 ios=5 input=small_io.dat 
CPU Utilization: 32.6497277676951                                                                                                                      IO Utilization: 83.15789473684211                                                                                                                      Average Turnaround Time: 469.1                                                                                                                         Average Wait Time: 0.0                                                                                                                                 Average I/O Wait Time: 60.1 

## python3 sim.py sched=FCFS cpus=5 ios=5 input=small_cpu.dat
CPU Utilization: 96.6604823747681                                                                                                                      IO Utilization: 8.051948051948052                                                                                                                      Average Turnaround Time: 494.1                                                                                                                         Average Wait Time: 211.9                                                                                                                               Average I/O Wait Time: 0.0

## python3 sim.py sched=FCFS cpus=1 ios=1 input=small_cpu_test.dat
CPU Utilization: 98.9010989010989                                                                                                                      IO Utilization: 65.93406593406593                                                                                                                      Average Turnaround Time: 74.7                                                                                                                          Average Wait Time: 59.7                                                                                                                                Average I/O Wait Time: 0.0   

## python3 sim.py sched=RR timeslice=1 cpus=1 ios=1 input=small_cpu_test.dat
CPU Utilization: 98.9010989010989                                                                                                                      IO Utilization: 65.93406593406593                                                                                                                      Average Turnaround Time: 78.8                                                                                                                          Average Wait Time: 51.9                                                                                                                                Average I/O Wait Time: 11.9 

