from functions.get_files_info import get_files_info

def test_1():
    print("Result for the current directory:")
    print(get_files_info("calculator", "."))

def test_2():
    print("Result for the \'pkg\' directory:")
    print(get_files_info("calculator", "pkg")) 

def test_3():
    print("Result for the '/bin' directory")
    print(get_files_info("calculator", "/bin"))

def test_4():
    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))
    
def main():
    test_1()
    test_2()    
    test_3()
    test_4()

main()