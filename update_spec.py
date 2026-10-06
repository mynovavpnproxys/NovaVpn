with open('buildozer.spec', 'r') as f:
    c = f.read()
c = c.replace('title = My Application', 'title = Nova VPN')
c = c.replace('package.name = myapp', 'package.name = novavpn')
c = c.replace('package.domain = org.test', 'package.domain = com.novavpn')
c = c.replace('requirements = python3,kivy', 'requirements = python3,kivy,requests')
c = c.replace('#android.permissions = INTERNET', 'android.permissions = INTERNET, ACCESS_NETWORK_STATE')
with open('buildozer.spec', 'w') as f:
    f.write(c)
print('[✓] تنظیمات buildozer.spec با موفقیت به روزرسانی شد!')
