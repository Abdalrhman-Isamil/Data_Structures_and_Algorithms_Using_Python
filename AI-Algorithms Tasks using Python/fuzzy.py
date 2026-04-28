A = {
    'x1': 0.2,
    'x2': 0.5,
    'x3': 0.8
}

B = {
    'x1': 0.6,
    'x2': 0.3,
    'x3': 0.4
}

# !(Union)
def fuzzy_union(A, B):
    result = {}
    for key in A:
        result[key] = max(A[key], B[key])
    return result

# !(Intersection)
def fuzzy_intersection(A, B):
    result = {}
    for key in A:
        result[key] = min(A[key], B[key])
    return result

#!(Complement)
def fuzzy_complement(A):
    result = {}
    for key in A:
        result[key] = 1 - A[key]
    return result

print("Union:", fuzzy_union(A, B))
print("Intersection:", fuzzy_intersection(A, B))
print("Complement of A:", fuzzy_complement(A))