import re

w = 'nol odin dva tri chetire pyat shest sem vosem devyat'.split()
with open("symbols.txt") as f:
    s = f.readline()
    nums = re.findall(r'\S+', s)
    total = {}
    for n in nums:
        if re.fullmatch(r'\d+', n):
            if re.search(r'^[0-9]0[0-9]*0[0-9]$', n) or (len(n) > 3 and len(n) % 2 == 0 and re.search(r'[13579]$', n)):
                print(n)
                for d in re.findall(r'(\d)', n):
                    total[w[int(d)]] = total.get(w[int(d)], 0) + 1
        else:
            print(f'oshibka {n}')
    for k,v in total.items():
        print(f'{k}: {v}')
