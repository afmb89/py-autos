from helpers import clear_view, display_main_menu

def run():
    display_main_menu()

    option = input("Pick from 1-6: ")    
    clear_view()
    

if __name__ == '__main__':
    run()