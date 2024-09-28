num = 0
total = 0.0
max_val = None
min_val = None

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    print(fval)

    num += 1
    total += fval

    if max_val is None or fval > max_val:
        max_val = fval
    if min_val is None or fval < min_val:
        min_val = fval

print('ALL DONE')
print('Maximum:', max_val)
print('Minimum:', min_val)
