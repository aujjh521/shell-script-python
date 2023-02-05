#!/bin/bash

root_path="./result"

for i in {1..5}
do
path="$root_path$i"
echo "start $i th training, save path is $path"
python train.py \
    --path $path
done