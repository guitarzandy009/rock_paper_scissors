# Data Structures
# 1. Dictionaries
# 2. Lists / Arrays
# 3. Sets


# Lists

lst = [1, 1, 11, 7]
print(lst)

lst.append(2)
print(lst)

lst.remove(11)
print(lst)

lst.sort()
print(lst)

# Sets

st = {1, 1, 11, 7}
print(st)
st.add(1)
st.add(1)
st.add(11)
print(st)
st.add(12)
st.add(121)
print(st)

# Dictionaries

d = {
    'bob': 0,
    'sarah': 0
}

print(d['bob'])
d['bob'] += 1
print(d['bob'])
print(d)
d['andy'] = 11
print(d)
d['bob'] += 1
print(d['bob'])
print(d)
d['bob'] += 1
print(d['bob'])
print(d)