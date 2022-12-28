class Protocol:
    start_symbol = "%"
    end_symbol = "&"
    tags_delimiter = ";"
    tag_value_delimiter = ":"

    SUCCESS = 0x00

    # Errors
    BAD_PACKET = 0x01
    BAD_SKILL = 0x02
    SOMETHING_WRONG = 0x03
    ABSENT_SERVO_CHANNEL = 0x10
    ABSENT_SERVO_VALUE = 0x11
    ABSENT_MOOD = 0x12

    def prepare_packet(self, data: list) -> str:
        data_string = f"{self.tags_delimiter}".join(data)
        # return f"{self.start_symbol}{data_string}{self.end_symbol}"
        return f"{data_string}"

    def parse_packet(self, packet: str) -> list:
        # packets: list = packet.replace(self.start_symbol, "").replace(self.end_symbol, "").split(self.tags_delimiter)
        packets: list = packet.split(self.tags_delimiter)
        answer = list()
        for pack in packets:
            answer.append(tuple(pack.split(self.tag_value_delimiter)))
        return answer
