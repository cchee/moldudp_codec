# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# MoldUDP (http://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/moldudp64.pdf)
# Field byte size constants
SESSION_FIELD_LEN       = 10
SEQ_NUM_FIELD_LEN       = 8
MESSAGE_COUNT_FIELD_LEN = 2
MESSAGE_SIZE_FIELD_LEN  = 2

# Position constants
SESSION_OFFSET = 0
SEQ_NUM_OFFSET = SESSION_OFFSET + SESSION_FIELD_LEN
MSG_CNT_OFFSET = SEQ_NUM_OFFSET + SEQ_NUM_FIELD_LEN
PAYLOAD_OFFSET = MSG_CNT_OFFSET + MESSAGE_COUNT_FIELD_LEN

# Packet byte size constants
MTU_SIZE     = 1500
UDP_HDR_SIZE = 8
HEADER_SIZE  = PAYLOAD_OFFSET
PAYLOAD_SIZE = MTU_SIZE - UDP_HDR_SIZE - HEADER_SIZE
MOLDPKT_SIZE = HEADER_SIZE + PAYLOAD_SIZE

# Packet Type constants
HEART_BEAT     = 0
END_OF_SESSION = 65535 # hex: 0xFFFF
