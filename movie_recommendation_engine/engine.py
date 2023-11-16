import data_initializer

candidates = data_initializer.initialize_data_from_json()

for candidate in candidates:
    print(candidate)

