def all_friends(school_friends,college_friends):
    return tuple(set(school_friends)|set(college_friends))

school_friends=["john","alice","bob","david"]
college_friends=["alice","charlie","david","eve"]

print(f"school friends: {school_friends}")
print(f"college friends: {college_friends}")

all_friends = all_friends(school_friends,college_friends)
print(f"all friends set | operator : {all_friends}")