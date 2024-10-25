import math

def calculate_similarity(model, base_word, target_word):
    if model is None or base_word is None or target_word is None:
        return 0

    if base_word not in model or target_word not in model:
        return 0

    sum_AB = sum_A = sum_B = 0

    base_vector = model[base_word]
    target_vector = model[target_word]

    if not base_vector or not target_vector or all(v == 0 for v in base_vector) or all(v == 0 for v in target_vector):
        return 0

    # formulata = A * B / (|A| * |B|)
    for i in range(len(base_vector)):
        sum_AB += base_vector[i] * target_vector[i]
        sum_A += base_vector[i] ** 2
        sum_B += target_vector[i] ** 2

    result  = sum_AB / (math.sqrt(sum_A) * math.sqrt(sum_B))

    return result

def find_most_similar_to_given(model, given_word, target_words):
    cosine_similarity = []

    if model is None or given_word is None or target_words is None:
        return 0

    for target in target_words:
        similarity = calculate_similarity(model, given_word, target)
        cosine_similarity.append(similarity)

    if not cosine_similarity:
        return 0

    return target_words[cosine_similarity.index(max(cosine_similarity))]

def doesnt_match(model, given_words):
    if model is None or not given_words:
        return 0

    cosine_similarity = []
    overall_sum = []

    for word in given_words:
        cosine_similarity.append([])
        overall_sum.append(0)

        for comparison_word in given_words:
            similarity = calculate_similarity(model, word, comparison_word)
            cosine_similarity[-1].append(similarity)

        overall_sum[-1] += sum(cosine_similarity[-1])

    return given_words[overall_sum.index(min(overall_sum))]