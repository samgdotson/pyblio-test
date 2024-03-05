import os
import traceback
from pybliometrics.scopus import ScopusSearch, AbstractRetrieval
import json
from tqdm import tqdm
import itertools

year = 2024
search_string = f"TITLE-ABS-KEY(energy justice)"
x = ScopusSearch(query=search_string, view='STANDARD')

print(x.results)