from load_csv import load


dataset = load("life_expectancy_years.csv")
print("\nTEST 1\nprintig the first 5 row from the dataset\n")
print(dataset.head(1))
print("\nTEST 2\nfuull dataset\n")
print(dataset)

baddataset = load("nani.wtf")
print(baddataset)
