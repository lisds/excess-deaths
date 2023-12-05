""" Fetch and validate data
"""

from pathlib import Path
import requests
import hashlib

file_info = {
    # Dictionary with key values pairs, where keys are output filenames
    # and values are dictionaries with keys URL and SHA1 hash.
    'vaccine_types.xlsx': {
        'url': 'https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/xlsx/data.xlsx',
        'sha1': '1051efcaabfe1ac83cd112b46ca7962c1985d489'},
    'excess_death.xlxs.xlsx': {
        'url': None,
        'sha1': '7e79a78219a98a7770d57ce15aef12c45cea29f5'}
}

data_path = Path('data')

for fname, info in file_info.items(): 
    out_path = data_path / fname
    if info['url'] is not None :
        r = requests.get(info['url'])
        out_path.write_bytes(r.content)
    assert hashlib.sha1(out_path.read_bytes()).hexdigest() == info['sha1']

print('Fetch and validation passed')

