import random
import numpy as np
def gen_money_like_str():
    appear_prob_bound = [0.1, 0.2, 0.3, 0.95, 1, 1, 1, 1]
    txt = []
    for i in range(8):
        tried = random.uniform(0, 1)
        if tried < appear_prob_bound[i]:
            num = random.randint(0, 9)
            txt.append(str(num))
    txt = np.array(txt)
    replace_prob = 0.3
    tried = random.uniform(0, 1)
    if tried < replace_prob:
        type_replace = random.choice([1, 2, 3, 4, 5, 6])
        if type_replace == 1:
            txt[:] = '0'
        elif type_replace == 2:
            txt[:] = '8'
        elif type_replace == 3:
            txt[-3:] = '0'
        elif type_replace == 4:
            txt[-3:-1] = '0'
        elif type_replace == 5 and len(txt) > 4:
            txt[-4:-1] = '0'
        elif type_replace == 6 and len(txt) > 4:
            txt[-4:-2] = '0'
    txt = txt.tolist()
    add_dot_prob = 0.2
    tried = random.uniform(0, 1)
    if tried < add_dot_prob:
        if len(txt) >= 7:
            txt = txt[: - 6] + ['.'] + txt[-6: -3] + ['.'] + txt[-3:]
        elif len(txt) >= 4:
            txt = txt[: -3] + ['.'] + txt[-3:]
    return ''.join(txt)
with open ('/home/asi/camera/thamnt/det_train/meter_reg/train_final/langdata/my7seg.training_text', 'w') as f:
    for i in range(10000):
        num = gen_money_like_str()
        f.write(num + '\n')






