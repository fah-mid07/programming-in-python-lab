  resources = [
[101, "Laptop", "Electronics", 8],
[102, "Projector", "Electronics", 0],
[103, "Whiteboard", "Classroom", 5],
[104, "Microphone", "Audio", 3],
[105, "Camera", "Electronics", 2]
 ]

def display_resources(resources):
     for resource in resources:
        print(resource)
display_resources(resources)

def search_by_category(resources, category):
  for resource in resources:
    if resource[2] == category:
        print(resource)
search_by_category(resources, "Electronics")  

def find_unavailable_resources(resources):
  for resource in resources:
     if resource[3] == 0:
        print("unavailable resource:", resource[1])
find_unavailable_resources(resources)      
