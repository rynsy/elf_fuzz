# ELF Fuzz

A simple ELF executable fuzzer. Wrote this up after watching a [LiveOverflow video](https://www.youtube.com/watch?v=OZvc-c1OLnM) on ELF parser differentials. 

It's very similar to the one in the [LiveOverflow repo](https://github.com/LiveOverflow/liveoverflow_youtube/tree/master/0x07_0x08_uncrackable_crackme) for that video, but I adapted
the code to work for Python3.5 and to use subprocess instead of system() to make the system calls. I did this so I could timeout any fuzzed executables that took too much time. 
I also added a make file to quickly build and clean things up.
