def ext(input_file, output_file):
    f=open(input_file, 'r')
    fp=open(output_file, 'w')
    i=-1
    j=-1
    line=f.readline()
    ch='"value": "'
    while line!="":
        if (line.find(ch)!=-1):
            value_start = line.find(ch) + len(ch)
            value = line[value_start:-3]
            fp.write(value + "\n")
            print("wait")
        line=f.readline()

def ext2(input_file, output_file):
        f=open(input_file, 'r')
        f2=open("the people that don fllow back.txt", 'w')
        i = 0
        for line in f:
            test = False
            fp=open(output_file, 'r')  
            for line2 in fp:
                if line.strip() == line2.strip():
                    test = True
                    break
            if not test:
                i += 1
                new_line = f"people N°{i}: {line}"
                print(new_line)
                f2.write(new_line)
            fp.close()
ext("following.json", "following after extracting.txt")
ext("followers_1.json", "followers after extracting.txt")
ext2("following after extracting.txt", "followers after extracting.txt")
print("done")
print("This script was developed by Hazem")
