#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 08:39:40 2023

@author: hyunseo
"""
import subprocess

#trial number
print("Trial number:")
trial_number = input()

#extract bandwidth size as a string
def bandwidth_extract():
    #linux shell command for iperf3 bidirection is given
    ls_process = subprocess.Popen(['cat', 'config.cfg'], stdout=subprocess.PIPE, text=True)
    
    grep_process = subprocess.Popen(["grep", "bandwidth"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)
    
    output, error= grep_process.communicate()
    
    x = output.split(' ')
    x_5 = x[-1]
    
    x_5=x_5[0:2]
    bandwidth_size = x_5
    return bandwidth_size

#extract tx_gain as a string
def txgain_extract():
    #linux shell command for iperf3 bidirection is given
    ls_process = subprocess.Popen(['cat', 'config.cfg'], stdout=subprocess.PIPE, text=True)
    
    grep_process = subprocess.Popen(["grep", "tx_gain"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)
    
    output, error= grep_process.communicate()
    
    x = output.split(' ')
    x_5 = x[-1]
    
    x_5=x_5[0:2]
    txgain = x_5
    return txgain

#extract rx_gain as a string
def rxgain_extract():
    #linux shell command for iperf3 bidirection is given
    ls_process = subprocess.Popen(['cat', 'config.cfg'], stdout=subprocess.PIPE, text=True)
    
    grep_process = subprocess.Popen(["grep", "rx_gain"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)
    
    output, error= grep_process.communicate()
    
    x = output.split(' ')
    x_5 = x[-1]
    
    x_5=x_5[0:2]
    rxgain = x_5
    return rxgain

# #extract dl_slots as a string
def dlslots_extract():
    #linux shell command for iperf3 bidirection is given
    ls_process = subprocess.Popen(['cat', 'config.cfg'], stdout=subprocess.PIPE, text=True)
    
    grep_process = subprocess.Popen(["grep", "dl_slots"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)
    
    output, error= grep_process.communicate()
    
    x = output.split(' ')
    x_5 = x[-1]
    
    x_5=x_5[0:1]
    dl_slots = x_5
    return dl_slots

#extract ul_slots as a string
def ulslots_extract():
    #linux shell command for iperf3 bidirection is given
    ls_process = subprocess.Popen(['cat', 'config.cfg'], stdout=subprocess.PIPE, text=True)
    
    grep_process = subprocess.Popen(["grep", "ul_slots"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)
    
    output, error= grep_process.communicate()
    
    x = output.split(' ')
    x_5 = x[-1]
    
    x_5=x_5[0:1]
    ul_slots = x_5
    return ul_slots

#extract N_ANTENNA_DL as a string

def N_ANTENNA_DL_extract():
    #linux shell command for iperf3 bidirection is given
    ls_process = subprocess.Popen(['cat', 'config.cfg'], stdout=subprocess.PIPE, text=True)
    
    grep_process = subprocess.Popen(["grep", "#define N_ANTENNA_DL"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)
    
    output, error= grep_process.communicate()
    x = output.split(' ')
    
    N_ANTENNA_DL = x[-2]
    return N_ANTENNA_DL

def N_ANTENNA_UL_extract():
    #linux shell command for iperf3 bidirection is given
    ls_process = subprocess.Popen(['cat', 'config.cfg'], stdout=subprocess.PIPE, text=True)
    
    grep_process = subprocess.Popen(["grep", "#define N_ANTENNA_UL"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)
    
    output, error= grep_process.communicate()
    x = output.split(' ')
    
    N_ANTENNA_UL = x[-1]
    return N_ANTENNA_UL


bandwidth_size = bandwidth_extract()
txgain = txgain_extract()
rxgain = rxgain_extract()
dl_slots = dlslots_extract()
ul_slots = ulslots_extract()
n_antenna_dl = N_ANTENNA_DL_extract()
n_antenna_ul = N_ANTENNA_UL_extract()
print(bandwidth_size, txgain, rxgain, dl_slots, ul_slots, n_antenna_dl, n_antenna_ul)


#distances
dist_list = ["1", "5", "10", "15", "20", "25", "30", "35"]
dist_name = ""

# get the distances from the "dis"
for i in range(len(dist_list)):
    dist_name += dist_list[i]+"m_"
dist_name = dist_name[0:-1]
print(dist_name)

# full name is designated
save_file_name = trial_number +"_"+"TR_Number_" + dl_slots+"DL_"+ul_slots+"UL_" + "_" + bandwidth_size+"MHz_"+txgain+"dB_"+rxgain+"dB_"+str(n_antenna_dl)+"[DL-ANT]_"+str(n_antenna_ul)+"[UL-ANT]_"+dist_name+".txt"

print(save_file_name)

subprocess.call(['touch', save_file_name])
