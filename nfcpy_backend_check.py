import nfc
clf = nfc.ContactlessFrontend()
print(clf.open('usb'))
