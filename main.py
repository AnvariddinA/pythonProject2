import winreg
keyValue = 'Software'
key =winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyValue)
winreg.SetValue(key, 'KIUF', winreg.REG_SZ, "KOREYA")

keyValue = r'Software\\KIUF'
key=winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyValue)
key=winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyValue)
key=winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyValue, access=winreg.KEY_ALL_ACCESS,)

winreg.SetValue(key,'IKT', winreg.REG_SZ, "Internet va axborot kommunikatsiyasi")
winreg.SetValue(key,'Guruh1', winreg.REG_SZ, "A guruh")
winreg.SetValue(key,'Guruh2', winreg.REG_SZ, "B guruh")

winreg.SetValueEx(key, "NewKey1",0, winreg.REG_SZ, "Yangi Qiymat 122354")
a=winreg.QueryValueEx(key, 'Newkey1')
print(a)
if key:
    winreg.CloseKey(key)


