from sys import argv, exit
from functools import partial
from pathlib import Path
from shutil import copyfileobj
from requests import get
from tqdm.auto import tqdm


def download(url, filename):
    print(filename)
    print("Downloading...")
    
    r = get(url, stream=True, allow_redirects=True)
    if r.status_code != 200:
        r.raise_for_status()  # Will only raise for 4xx codes, so...
        raise RuntimeError(f"Request to {url} returned status code {r.status_code}")
    file_size = int(r.headers.get('Content-Length', 0))

    path = Path(filename).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    desc = "(Unknown total file size)" if file_size == 0 else ""
    r.raw.read = partial(r.raw.read, decode_content=True)  # Decompress if needed
    with tqdm.wrapattr(r.raw, "read", total=file_size, desc=desc) as r_raw:
        with path.open("wb") as f:
            copyfileobj(r_raw, f)

    print("Complete!")
    print("Downloaded to", path)

if len(argv) == 2:
    # take system argument as string
    url = argv[1]

    filename = url.split('/')[-1]
    filename = filename.split('?')[0]

    download(url, filename)

elif len(argv) == 3:
    # take system argument as string
    url = argv[1]
    filename = argv[2]

    # Getting the file extension
    name = url.split('/')[-1]
    name = name.split('?')[0]
    file_extension = name.split('.')[-1]


    filename = filename + '.' + file_extension

    download(url, filename)

else:
    print("Usage: fileD '<url>' <filename>")
    exit(1)