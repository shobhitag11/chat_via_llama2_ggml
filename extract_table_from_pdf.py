from tabula import read_pdf
from tabulate import tabulate
import camelot
# from ctypes.util import find_library
# find_library("gs")

# extract all the tables in the PDF file
# abc = camelot.read_pdf("table.pdf")  # address of file location

# print the first table as Pandas DataFrame
# print(abc[0].df)

# # reads table from pdf file
df = read_pdf("sample.pdf", pages="all", multiple_tables=True)  # address of pdf file
print(df)
print("---------------")
print(tabulate(df[0]))