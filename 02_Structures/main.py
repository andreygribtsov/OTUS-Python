
fn = lambda x: x*x
print(f"test map function", list(map(fn,range(10))))

print(f"test filter function", list(filter(lambda x: x%2 == 0, range(10))))

print(f"test decorator")

def decorator(fn):
    def wrapper(*args, **kwargs):
        print(fn(*args, **kwargs))
    return wrapper

@decorator
def calculate_avg(lst):
    return sum(lst)/len(lst)
        

lst = list(range(50))
calculate_avg


















