﻿# MinimumPlatforms
You are given the arrival and departure times of some trains in 24-
hour format. Your task is to determine the minimum number of
platforms needed at a railway station to accommodate all trains
arriving and departing (i.e. ensuring that no two trains overlap at a
single platform and no train is left waiting).
All trains arrive and depart on the same day, with distinct arrival and
departure times. To prevent conflicts, separate platforms are needed
for trains whose arrival overlaps with the departure of another train
on the same platform.
Write a program that reads the arrival and departure times of the
trains in 24-hour format and prints the minimum number of platforms
needed at a railway station to accommodate all trains.
#Input
The first line of input contains space-separated integers representing
the arrival times of the trains in 24-hour format.
The second line of input contains space-separated integers
representing the departure times of the trains in 24-hour format.
#Output
The output should be single line containing an integer representing
the minimum number of platforms needed to accommodate all
arriving and departing trains without any overlap or delays.
#Explanation
For example, consider the following arrival and departure times of 5
trains:
trains arrival timings = 0900 0940 0950 1100 1500
