from functions.get_file_content import get_file_content

def test_1():
    print("Result for lorem.txt")
    print(get_file_content("calculator", "lorem.txt"))

def test_2():
    print("Result for main.py")
    print(get_file_content("calculator", "main.py"))

def test_3():
    print("Result for pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))

def test_4():
    print("Result for /bin/cat")
    print(get_file_content("calculator", "/bin/cat"))

def test_5():
    print("Result for pkg/does_not_exist.py")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    
def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()

main()