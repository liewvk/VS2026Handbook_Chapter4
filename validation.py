sample_inputs = ['5', '-2', 'three']
for raw in sample_inputs:
    try:
        number = int(raw)
        print('Accepted' if number > 0 else 'Invalid quantity')
    except ValueError:
        print('Enter a whole number')

