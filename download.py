import wget

print('Beginning file download with wget module')

url = 'https://www.google.com/recaptcha/api2/payload/audio.mp3?p=06AOLTBLQJV3twv1ifW-aQouWL-lZxrrAa4l4K7yZb8RgVbIb0lbUDcK0T2q7XIE_0SdzPY3bN-DBGGS8u_CVikP_2e5kTy7lB2ltDYiwRmGurQTr-K2Z1k7goy8Og9_HrlYzQdJnrtUxwoFO9-0KOPZk7DBwpZpX-beOPHPTZLYAts5FGgmHm1S4&k=6LfzijMUAAAAACRHPUtzyKDeqEtqSmWOuJS3duAj'
wget.download(url, '/Users/KillaShank/desktop/yo.mp3')
