Place input traces into the input directory and run python timestamp-to-iat.py. Output traces will be found in the output directory.

Input Format (unix timestamp): each line is a unix timestamp that logs the time at which a packet was received.

Output Format (IAT: inter-arrival time): each line corresponds to a packet being received and logs the time in milliseconds (rounded to the nearest millisecond) since the first packet was received.
