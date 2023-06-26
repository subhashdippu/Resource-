for i in range(2, 21):
    with open(f"tab/table1.txt{i}", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j}") 