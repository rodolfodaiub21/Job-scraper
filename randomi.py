with open('text.txt','r') as file:
    text=file.read()    
count = len(text.split())
print(f"Word count: {count}")
