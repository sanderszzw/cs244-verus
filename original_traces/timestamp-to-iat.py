#! /usr/bin/python
import os


INPUT_DIR = "input"
OUTPUT_DIR = "output"


def main():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for input_filename in os.listdir(INPUT_DIR):
        output_filename = "%s.out" % input_filename
        print("Converting %s to inter-arrival times and saving as %s..." % (input_filename, output_filename))
        with open("%s/%s" % (INPUT_DIR, input_filename), 'r') as infile, open("%s/%s" % (OUTPUT_DIR, output_filename), 'w+') as outfile:
            initial = None
            for line in infile:
                if initial is None:
                    initial = float(line)
                difference = float(line) - initial
                output = int(round(difference * 1000))
                outfile.write("%d\n" % output)


if __name__ == '__main__':
    main()
