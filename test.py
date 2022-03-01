names = ['daniel', 'john', 'cairo', 'anna']
score_round1 = [1, 2, 3, 0]
score_round2 = [3, 4, 3, 0]
score_round3 = [5, 6, 3, 0]
#score_round4 = [2, 4, 2]
total_score = []


def test():
    
    zipped_lists = zip(score_round1, score_round2, score_round3)
    total_score = [x + y + z for (x, y, z) in zipped_lists]
    print(total_score)
    result = {}
    for i,j in zip(names,total_score):
        result[i] = j
    print(result)
    
test()