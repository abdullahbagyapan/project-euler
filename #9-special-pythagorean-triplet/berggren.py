from collections import deque


# Berggren's linear transformations as functions
def A(triple):
    a,b,c = triple
    return ( a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c )

def B(triple):
    a,b,c = triple
    return ( a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c )

def C(triple):
    a,b,c = triple
    return ( -a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c )



def berggren(target_sum):
    
    queue = deque([(3, 4, 5)])  # start from the root primitive triple
    
    matrices = [A, B, C]

    while queue:
        a, b, c = queue.popleft()
        total = a + b + c
        
        # check if scaling reaches target sum
        if target_sum % total == 0:
            k = target_sum // total
            return (k*a, k*b, k*c)
        
        # generate children only if their sum <= target_sum
        for f in matrices:
            child = f((a, b, c))
            if sum(child) <= target_sum:
                queue.append(child)
    
    return None


# A + B + C = 1000 = N
N = 1000

triple = berggren(N)

print("Triple:", triple)                                # Output should be (375, 200, 425)

print("Product abc =", triple[0]*triple[1]*triple[2])   # Output should be 31875000


# Relative Links:
# https://en.wikipedia.org/wiki/Pythagorean_triple#Parent/child_relationships