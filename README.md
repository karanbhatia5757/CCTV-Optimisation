# CCTV Footage -Optimisation
This repository contains code for optimisation of CCTV clip in both size and duration.<br/> 
The code is written in python and uses opencv library.<br/>
The approach used is pretty simple. Most of the clip in a CCTV security camera is still with very less motion or changes.<br/>
This is due to repetitive frames. So, the approach uses Mean Squared Error between pixels of adjacent frames and compares this with threshold.<br/>
If the error is more than the threshold, then there is a significant difference that can be detected by human eye between the frames and we do not delete it. Otherwise, it is removed from the memory.<br/>



