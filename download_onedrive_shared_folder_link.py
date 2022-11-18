# download onedrive shared folder link
import os, wget
from tqdm import tqdm

### inputs
# find div "ms-SelectionZone" and copy and paste the html code
div_html = """
<div class="ms-SelectionZone" role="presentation"><div class="ms-FocusZone css-45 ms-TilesList" data-focuszone-id="FocusZone31">~~~~</div></div></div></div></div></div></div></div></div>
"""

# write the shared folder link
shared_folder_link = 'https://onedrive.live.com/?authkey=XXX&id=XXX'

# write download path
path_download = os.path.join(os.getcwd(), 'download')
###

params = {x.split('=')[0]: x.split('=')[1] for x in shared_folder_link.split('?')[-1].split('&')}
for k, v in params.items():
    print(k, ':\t', v)

resid_list, url_list = [], []
for line in div_html.replace('><', '>\n<').split('\n'):
    if params['id'] in line:
        resid = line.split('id=')[-1].split('&')[0]
        if resid not in resid_list:
            resid_list.append(resid)
            url = 'https://onedrive.live.com/download?authkey={}&resid={}'.format(params['authkey'], resid)
            url_list.append(url)
            print(len(url_list), url)

os.makedirs(path_download, exist_ok=True)
print('Created directory:', path_download)

print('Downloading {} files...'.format(len(url_list)))
for url in tqdm(url_list[:3]):
    wget.download(url, path_download)
    print('Downloaded:', url, 'to', path_download)
