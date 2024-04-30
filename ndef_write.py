import nfc
from nfc.clf import RemoteTarget
from ndef import TextRecord, message

def write_ndef(uri):
    clf = nfc.ContactlessFrontend('usb')  # USB 연결된 NFC 리더기 사용

    target = clf.sense(RemoteTarget('106A'), iterations=10, interval=0.1)
    if target is None:
        print("No NFC tag found")
        return

    tag = nfc.tag.activate(clf, target)
    ndef_message = message(TextRecord(uri))  # NDEF 메시지 생성

    if tag.ndef:
        tag.ndef.records = [ndef_message]  # NDEF 레코드 쓰기
        print("NDEF message written to the tag")
    else:
        print("This tag is not NDEF-formattable.")

    clf.close()

if __name__ == "__main__":
    write_ndef("Hello, NFC!")
