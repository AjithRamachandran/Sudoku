from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import ctypes
import numpy as np

my_url = 'http://www.menneske.no/sudoku/eng/'

def create_soup():
    client = urlopen(my_url)
    html = client.read()
    client.close()

    bsoup = soup(html, "html.parser")

    rows = bsoup.find_all('tr', {'class':'grid'})
    sudoku = []
    raw_data = []

    for row in rows:
        cols = row.find_all('td')
        rows_ = []
        for col in cols:
            txt = col.text
            if(txt.isdigit()):
                rows_.append(txt)
            else:
                rows_.append('0')
        raw_data.append(rows_)

    for i in raw_data:
        i = list(map(int, i))
        sudoku.append(i)
    
    return sudoku

sudoku = create_soup()

libc = ctypes.cdll.LoadLibrary('./libc.so')
sudoku = np.array(sudoku)
sudoku = sudoku.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
if((libc.solveSudoku(sudoku))):
    libc.printGrid(sudoku)