def create_mock_data(filename, rows):

    with open(filename, 'wt') as f:
        for i in range(rows):
            patient_ID = i
            heart_rate = 100 + i % 20
            f.write(f'{patient_ID},{heart_rate}')

if __name__ == "__main__":
    create_mock_data('data.txt', 100)