from cache import append_data, read_data
from scraper import get_protein

def main():
    data = get_protein("Chase")
    append_data(data)

if __name__ == '__main__':
    main()