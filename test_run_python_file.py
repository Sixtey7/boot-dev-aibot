from functions.run_python_file import run_python_file

def test_1():
    print (run_python_file("calculator", "main.py"))

def test_2():
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

def test_3():
    print(run_python_file("calculator", "tests.py"))

def test_4():
    print(run_python_file("calculator", "../main.py"))

def test_5():
    print(run_python_file("calculator", "nonexistent.py"))

def test_6():
    print(run_python_file("calculator", "lorem.txt"))
    
def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()

main()