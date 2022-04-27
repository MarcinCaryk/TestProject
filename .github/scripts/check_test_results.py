import argparse
import xml.etree.ElementTree as ET

def check_if_there_are_fails(path):
    tree = ET.parse(path)

    root = tree.getroot()
    if int(root.attrib['failures']) != 0:
        raise Exception('Number of tests failed  {}'.format(int(root.attrib['failures'])))
    print(root.attrib)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if test fails test")

    parser.add_argument("-jxml",  help="path to xml junit file results")
    args = parser.parse_args()
    print(args.jxml)
    check_if_there_are_fails(args.jxml)
