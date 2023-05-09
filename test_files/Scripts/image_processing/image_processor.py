def process_file():
    path = '/Users/charlienorgaard/Desktop/CubeSat/'
    input_file = path + 'image_string.txt' 
    output_file = open(path + 'processed_image_1.txt', 'w')
    with open(input_file) as f:
        lines = f.readlines()[1:]
        for line in lines:
            line = line.strip().split()
            if len(line) > 0:
                if line[-1] != 'IMAGE' and line[-1] != 'TEST':
                    output_file.write(line[-1])          


def main():
    process_file()


if __name__ == '__main__':
    main()