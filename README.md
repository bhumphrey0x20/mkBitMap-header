# mkBitMap-header
Python script uses openCV to read an image and create a bitmap file.
The script creates C-style .h file with a uint32_t array containing the pixel files as array elements.
The element pixels are in the format 0xrRRGGBBAA, where RR, GG, BB are the red, green and blue channel pixels, and AA is the alpha channel.
