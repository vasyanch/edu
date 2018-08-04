import os
answer = []
for a in os.walk('.'):
    for k in a[2]:
        if '.py' in k:
            answer.append(a[0][2:])
            break
with open('found_dir.txt', 'w') as out:
    for i in answer:
        out.write(i + '\n')

    
