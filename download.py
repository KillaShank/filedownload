import wget

print('Beginning file download with wget module')

url = 'https://filmisongs.com/charlie-puth-attention-mp3-download-song-2019/'
wget.download(url, '/Users')
