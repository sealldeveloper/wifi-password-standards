import os

if os.path.isfile('netgear-spectrum-nums.txt'):
    os.remove('netgear-spectrum-nums.txt')

with open('netgear-spectrum.txt','r') as f:
    data=f.readlines()
    f.close()
c=0
t=0
current_percentage=0
for x in data:
    t+=1
with open('netgear-spectrum-nums.txt','a') as f:
    for x in data:
        for number in range(1000):
            x=x.replace("\n","").replace("\r","")
            f.write(f'{x}{number:03d}\n')
            if round(c/(t*999)*100) != current_percentage:
                current_percentage=round(c/(t*999)*100)
                print(f'Current count: {c}/{t*999} ({round(c/(t*999)*100)}%)')
            c+=1
    f.close()
print(f'Final count: {c}')
