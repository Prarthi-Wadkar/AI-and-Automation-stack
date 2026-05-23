def describe_product(name, audience, budget=0):
    return f"{name} is built for {audience} with {budget} budget"

print(describe_product("first users", "indie founders", 0))

channels = ["reddit", "twitter", "discord", "linkedin"]
uppercase = [c.upper() for c in channels]
print(uppercase)

dict ={
    "name" : "prarthi",
    "product" : "first users",
    "audience" : "indie founders",
    "budget" : 0
}

for key, value in dict.items():
    print(f"{key}: {value}")

    try:
        result = int("not a number")
    except ValueError as e:
       print(f"caught error: {e}")

def idk(name, fav_timepass, hobby):
    return f"{name} does {fav_timepass} for timepass and {hobby} for hobby!"

print(idk("prarthi","sleeping","coding"))
