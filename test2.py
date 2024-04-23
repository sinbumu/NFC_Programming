import nfc

def on_connect(tag):
    print("\nConnected to NFC Tag")
    print("Type:", tag.type)
    print("ID:", tag.identifier.hex())
    if tag.ndef:
        for record in tag.ndef.records:
            print("NDEF Record:")
            print("  TNF:", record.tnf)
            print("  Type:", record.type)
            print("  ID:", record.id)
            print("  Payload:", record.payload)
    return True

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': on_connect})
