#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

#test that if N is too big insert_..pairs.py doesn't work
run N_test python insert_key_value_pairs.py rand.txt hash 1000000
assert_exit_code 1

#test if grapher.py makes graphs

rm Insert_Time_rand.jpg
rm Search_rand.jpg
rm Search_Not_There_rand.jpg

test ! -f Insert_Time_rand.jpg
test ! -f Search_rand.jpg
test ! -f Search_Not_There_rand.jpg

python grapher.py rand.txt rand_not.txt 10

test -f Insert_Time_rand.jpg
test -f Search_rand.jpg
test -f Search_Not_There_rand.jpg

test ! -f Insert_Time_sorted.jpg
test ! -f Search_sorted.jpg
test ! -f Search_Not_There_sorted.jpg

python grapher.py sorted.txt rand_not.txt 10

test -f Insert_Time_sorted.jpg
test -f Search_sorted.jpg
test -f Search_Not_There_sorted.jpg
