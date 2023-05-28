import argparse
import os
import re
def convert_dir2href(dir, pattern):
    # Remove the base directory from the text
    pattern = re.escape(pattern)
    dir = re.sub(pattern, "", dir)
    linux_path = dir.replace("\\", "/")
    linux_path = "." + linux_path
    return linux_path

def sort_func(name):
    # Get the string integer from the file name
    temp = re.findall(r'\d+', name)

    if temp:
        return int(temp[0])
    else:
        # The maximum book index is 9999999
        return 9999999


if __name__ == "__main__":
    # Get the file location from the python parser
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', nargs='?', help="name of the employee")
    args = parser.parse_args()

    current_directory = args.dir
    # Save a pattern to make text subtraction
    pattern = current_directory
    stack=[[current_directory, -1]]

    indent = "  "
    book_list = "# Summary\n\n"
    while stack:
        data = stack.pop()
        current_directory = data[0]
        title_name = os.path.basename(current_directory)

        names = sorted(os.listdir(current_directory), key=sort_func, reverse=True)
        for name in names:
            file = current_directory + "\\" + name
            if name == "README.md" and title_name != "docs":
                template = "{indent}* [{title}]({href})"
                href = convert_dir2href(file, pattern)
                template = template.format(indent=indent*data[1], title=title_name, href=href)
                book_list = book_list + template + "\n"

            if os.path.isdir(file) and title_name != "docs":
                stack.append([file, data[1]+1])

    print(book_list)

    with open("SUMMARY.md", "w") as f:
        # Write text to the file
        f.write(book_list)


