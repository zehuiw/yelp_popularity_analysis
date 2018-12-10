import os

# os.system('source my_project/bin/activate')

with open('../GraphSAGE_input/bid.txt', 'r') as f:
    i = 0
    for line in f:
        i += 1
        if i <= 8000:
            continue
        bid = line[:-1]
        cmd = 'python -m graphsage.unsupervised_train --train_prefix ../GraphSAGE_input/%s --model graphsage_mean --epochs 10 --max_total_steps 1000 --validate_iter 1 --dim_1 10 --dim_2 10'%bid
        os.system(cmd)
