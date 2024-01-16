#Exercise: indexing and slicing

url = 'https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv'

#Use indexing, slicing to fill in the following output
#Copy/paste is not allowed

file_name = url[-14:]
print(file_name)  # 'ted-sample.csv'

protocol = url[:5]
print(protocol)  # 'https'

host_name = url[8:18]
print(host_name)  # 'github.com'

print(protocol + '://' + host_name + '/' + file_name)
#use string composition to construct https://github.com/ted-sample.csv
