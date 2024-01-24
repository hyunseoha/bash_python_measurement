Codes are constructed as follow.

work 1. sh_name_generator.sh is run.
   it calls files in [generator] folder.
   in [generator] there are two files.
      copy_shell.sh - it copies a config (called enb.cfg) file that sets the vRAN device configuration located /root/lteenb-linux-2023-09-08/config/. Using this script, it is always possible to get the current config file. So there is less false recording. it is kind of a fool proof work.
      name_generator.py - this script collects necessary radio information, such as MIMO or SISO, bandwidth and so on. In the end it makes a txt file with the collected information. This script can be updated to give a different distances. see the line #131.
      with those two files, txt files with the current radio information can be made and the recording work which is difficult at the field decreases.
      
work 2. command [python3 test_script.py | tee [the txt file made from work 1.]]
   test_script.py - it runs iperf3 bidirectional test with the given distances. it is designed to run the test multiple times with different parameters. the parameter was a distance on 05.oct.2023. before it is run, testers have to look into the script and adjust the parameter and change the script.
   command [tee] - it saves the results of iperf3 test into the given txt. from work 1. txt file names were already made, it is easy to choose one from them.

I actually wanted to make one script to do all this work. I will do it after the holiday.
