from smartcard.System import readers
from smartcard.util import toHexString

def read_nfc():
    # 사용 가능한 리더기 목록을 가져옵니다.
    r = readers()
    print("Available readers:", r)

    if not r:
        print("No readers found!")
        return

    reader = r[0]
    print("Using reader:", reader)

    try:
        # 리더와 카드 사이의 연결을 시작합니다.
        connection = reader.createConnection()
        connection.connect()

        # NFC 카드의 UID를 읽기 위한 APDU 명령입니다.
        # 이 명령은 ISO 14443 Type A 카드에 사용됩니다.
        GET_UID_APDU = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        data, sw1, sw2 = connection.transmit(GET_UID_APDU)

        if sw1 == 0x90 and sw2 == 0x00:
            # 성공적으로 UID를 읽었을 때
            print("Card UID:", toHexString(data))
        else:
            print("Failed to read card UID")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    read_nfc()
