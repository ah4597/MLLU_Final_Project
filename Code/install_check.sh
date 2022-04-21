#!/bin/bash
#general requirements
conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia -y
pip install datasets
pip install transformers
pip install nltk
pip install DeepSpeed
ds_report
