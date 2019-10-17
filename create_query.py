import transliterate

inp = "fio.txt"
out = "script.txt"
pass_list = "pass_list.txt"
group_list = {}
with open(inp, encoding="utf-8") as fh:
    for line in fh:
        print(line)
        fio = line.replace("\n", "")
        line = line.replace("\n", "").split(" ")[0]
        line = transliterate.translit(line, reversed=True)
        line = line.replace("'", "")
        group_list[fio] = line

print(group_list)

for key in group_list:
    fio = key
    surname = group_list[key]
    password = "".join(list(surname)[::-1])

    try:
        fh = open(pass_list, "a+", encoding="utf-8")
        fh.write("{}  Логин: {} Пароль: {}".format(fio, surname, password))
        fh.write("\n")
    finally:
        if fh:
            fh.close()

    try:
        fh = open(out, "a+", encoding="utf-8")
        fh.write("CREATE DATABASE "+surname+";\n"
                 "GO\n"
                 "create login "+surname+"\n"
                 "with password='"+password+"'\n"
                 "use "+surname+";\n"
                 "create user "+surname+" for login "+surname+"\n"
                 "with default_schema = dbo;\n"
                 "alter role db_owner add member "+surname+";\n"
                 "alter login "+surname+" with default_database = "+surname+";\n")
        fh.write("\n")
    finally:
        if fh:
            fh.close()
