import numpy as np
from skimage.metrics import structural_similarity as ssim

def compute_similarities(features):
    sites = list(features.keys())
    pairs = []
    for i in range(len(sites)):
        for j in range(i+1, len(sites)):
            s1, s2 = sites[i], sites[j]
            f1, f2 = features[s1], features[s2]

            hamming = f1['hash'] - f2['hash'] <= 5
            bhatt = np.sum(np.sqrt(f1['hist'] * f2['hist'])) >= 0.9
            ssim_score = ssim(f1['img'], f2['img'], data_range=1.0) >= 0.8

            if sum([hamming, bhatt, ssim_score]) >= 2:
                pairs.append((s1, s2))
    return pairs

def cluster_sites(features, similar_pairs):
    graph = {k: set() for k in features}
    for a, b in similar_pairs:
        graph[a].add(b)
        graph[b].add(a)

    visited = set()
    groups = []
    for site in graph:
        if site in visited:
            continue
        stack = [site]
        group = []
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            group.append(node)
            stack.extend(graph[node] - visited)
        groups.append(group)
    return groups
