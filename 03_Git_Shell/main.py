#%%
print(
    list((x*x for x in range(10)))
)

lst = list(range(20))
print(
    list(filter(lambda x: x%2 == 0, lst))
)

