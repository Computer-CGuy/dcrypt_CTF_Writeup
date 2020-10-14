### Challenge beef

After disassembling the binary I found a read_flag function that reads ``flag.txt`` just above the main function. So clearly it was a buffer overflow exploit


### Approaching the exploit

I ran the file in gdb and entered a string of random non repeating characters\
After taking the input it shows a SEGMENATION_FAULT meaning that we have overwrited the return funciton [gdb pauses the run after SEGMENTATION_FAULT]\
Then I used ``x/s $rsp`` to get the overflowed string and search for the part of the string overflowed, now I know more than 56 characters will cause overflow\
The read_flag function is at 0x00000000004011b6 hex in the binary file and we have to jump to the read_flag so adding ``\xb6\x11\x40\x00\x00\x00\x00\x00`` after the string will jump to the read_flag


### Code

``python -c 'print("dhdsudisd wdiwsdsdi DSUDH sdasui dwd9w  9 dsd sjdn sdpid"+"\xb6\x11\x40\x00\x00\x00\x00\x00")' | ./beef``
