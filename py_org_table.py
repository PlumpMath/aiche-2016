#!/usr/bin/env python

def string_to_number(s):
    'Try to convert S to a number, return S otherwise.'
    if '.' in s:  # possible float
        try:
            return float(s)
        except ValueError:
            return s
    else:
        try:
            return int(s)
        except ValueError:
            return s
    return s

def read_org_table(filename, tablename, include_header=True):
    '''Read the table named TABLENAME from the org-file named FILENAME.
    If not INCLUDE_HEADER, skip the first row of the table.'''
    with open(filename) as f:
        contents = f.readlines()
    # find the table name. Starts with a line like #+tblname:
    for i, line in enumerate(contents):
        if (line.lower().startswith('#+name')
            and tablename in line):
            table_name = i
            break

    # now find start of data
    table_data_start = table_name
    for line in contents[i:]:
        if line.startswith('|'):
            break
        else:
            table_data_start += 1

    # now read the data
    data = []
    for line in contents[table_data_start:]:
        if not line.startswith('|'):
            break
        elif line.startswith('|-'):
            continue
        row = [string_to_number(x.strip()) for x in line.strip().split('|')]
        data += [row[1:-1]]

    if include_header:
        return data
    else:
        return data[1:]


if __name__ == '__main__':
    import sys
    print(read_org_table(sys.argv[1], sys.argv[2]))
