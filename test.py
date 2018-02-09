import os
import glob

def quadrant_selection(x, y):
    if x > 0:
        return 1 if y > 0 else 4
    else:
        return 2 if y > 0 else 3

def test_cases():
    path = os.getcwd() + "/CCC/junior_data/j1/"
    for input_file_name in glob.glob(os.path.join(path, '*.in')):
        with open(input_file_name) as input_file_handle:
            lines = [line.strip() for line in input_file_handle]
            
            #invoke the function
            output = quadrant_selection(int(lines[0]),int(lines[1]))
            
            #test the function
            output_file_name = input_file_name[0:-2] + "out"
            with open(output_file_name) as output_file_handle:
                expected = int(output_file_handle.readline())
                print("passed" if output == expected else "expected: {0}, output: {1}".format(expected, output))

if __name__ == "__main__":
    test_cases()