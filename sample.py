def sample(a,b):
    try:
        return (a/b)
    except:
        return "b cannot be zero"
    finally:
        return 100
b=sample(10,5)
print(b)
print("new line")
