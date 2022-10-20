def function():
    class A:
        def __init__(self, filenames, dirnames):
            self.filenames = filenames
            self.dirnames = dirnames

    fileAndAdrresstemp1 = []
    files1 = []
    for (dir_path, dir_names, file_names) in sorted(os.walk(path_dir)):
        fileAndAdrresstemp1.append(A(file_names, dir_path))
        files1.extend(file_names)

    fileAndAdrress1 = []
    for t in fileAndAdrresstemp1:
        for file in t.filenames:
            fileAndAdrress1.append(A(file, t.dirnames))

    print("first Workspace")
    for i in fileAndAdrress1:
        print(i.filenames, i.dirnames, sep=' / ')

    fileAndAdrresstemp2 = []
    files2 = []
    for (dir_path, dir_names, file_names) in sorted(os.walk(path_dir1)):
        fileAndAdrresstemp2.append(A(file_names, dir_path))
        files2.extend(file_names)

    fileAndAdrress2 = []
    for t in fileAndAdrresstemp2:
        for file in t.filenames:
            fileAndAdrress2.append(A(file, t.dirnames))

    print("second workspace")
    for i in fileAndAdrress2:
        print(i.filenames, i.dirnames, sep=' / ')

    now = datetime.datetime.now().replace(microsecond=0)

    difference = difflib.HtmlDiff(wrapcolumn=200).make_file(files1, files2,
                                                            fromdesc=f'Right path: {path_dir}   Date:{now}',
                                                            todesc=f"Left path: {path_dir1}    Date:{now}")
    with open(path + 'difft.html', 'w') as diff_repo:
        diff_repo.write(difference)

function()