import requests
print(len(requests.get(open('dataset_3378_2.txt').readline().strip()).text.splitlines()))