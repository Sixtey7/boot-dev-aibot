from functions.write_file import write_file

def test_1():
    print("Writing to lorem.txt")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))


def test_2():
    print("test writing morelorem")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

def test_3():
    print ("test error case")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

def main():
    test_1()
    test_2()
    test_3()
    
main()