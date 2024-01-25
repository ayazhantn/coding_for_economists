#read text files

#open
file = open('data/raw/european_commission/ted-sample.csv')

print(file.readline())

file.close()

#here we have to close the file manually; not ideal

#context manager
with open('data/raw/european_commission/ted-sample.csv') as file:
  for line in file:
    print(line)