import itertools
import os
# slurm params
partition = 'high'

# python ../02_fit_logistic.py --dataset financial_phrasebank --checkpoint distilbert-base-uncased --subsample 1000 --ngrams 1 --all all --layer last_hidden_state_mean --seed 1

# # python ../02_fit_logistic.py --dataset financial_phrasebank --checkpoint distilbert-base-uncased --subsample 1000 --ngrams 1 --all all --layer last_hidden_state_mean --seed 1 --ignore_cache

# python ../02_fit_logistic.py --dataset financial_phrasebank --checkpoint bert-base-uncased --ngrams 1 --all all --layer last_hidden_state_mean --seed 1 --ignore_cache


GLOBAL_PARAMS = {
    'subsample': [-1],  # 100, 1000
    'seed': [1, 2, 3],
}

PARAMS_LIST = [
    {
        'dataset': ['emotion'],
        'checkpoint': [],
    },
    {
        'dataset': ['tweet_eval'],
        'checkpoint': [],
    },
    {
        'dataset': ['rotten_tomatoes'],
        'checkpoint': [],
    },
    {
        'dataset': ['financial_phrasebank'],
        'checkpoint': [],
    },
    {
        'dataset': ['sst2'],
        'checkpoint': [],
    },
]

CHECKPOINTS_SHARED = [
    'glove_wordvecs',
]

for i in range(len(PARAMS_LIST)):
    d = PARAMS_LIST[i]
    d['checkpoint'] = d['checkpoint'] + CHECKPOINTS_SHARED

# print(PARAMS_LIST)

num = 0
for PARAMS in PARAMS_LIST:
    ks = list(PARAMS.keys())
    vals = [PARAMS[k] for k in ks]

    ks2 = list(GLOBAL_PARAMS.keys())
    vals += [GLOBAL_PARAMS[k] for k in ks2]
    ks += ks2

    param_combinations_all = list(itertools.product(*vals))  # list of tuples
    param_combinations = param_combinations_all

    py = 'python'
    for i in range(len(param_combinations)):
        print(f'-------------------\n\n{num} / {len(param_combinations) * len(PARAMS_LIST)}\n---------------------\n')
        param_str = 'python ../03_fit_logistic.py '
        for j, key in enumerate(ks):
            param_str += '--' + key + ' ' + str(param_combinations[i][j]) + ' '
        # param_str += '--ignore_cache'
        # s.run(param_str)
        # print(param_str)
        num += 1
        os.system(param_str)