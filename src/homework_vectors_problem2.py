import math

def find_common_meaning(model, base_word, related_word, target_word):
    if model is None or base_word is None or related_word is None or target_word is None:
        return 0
    if base_word not in model or related_word not in model or target_word not in model:
        return 0

    base_word_vector = model[base_word]        
    related_word_vector = model[related_word]   

    sum_A = sum(x ** 2 for x in base_word_vector)
    sum_B = sum(x ** 2 for x in related_word_vector)
    sum_target = sum(model[target_word][i] ** 2 for i in range(len(base_word_vector)))

    result = math.sqrt(sum_A) * math.sqrt(sum_B) / math.sqrt(sum_target)

    sums = []
    common = {}
    all_results = []

    for key in model:
        if key == target_word:
            continue
        
        if len(model[key]) != len(base_word_vector):
            continue

        current_sum = sum(model[key][i] for i in range(len(base_word_vector)))
        sums.append(current_sum)

        common[key] = result / current_sum if current_sum != 0 else float('inf')
        all_results.append(abs(result / current_sum) if current_sum != 0 else float('inf'))

        print(common[key], key, all_results[-1])

    if all_results:
        return list(common)[all_results.index(min(all_results))]

    return None