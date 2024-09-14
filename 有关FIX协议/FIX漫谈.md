## FIX漫谈

- 在某些特定的业务中， 可能会要求某个特定MsgType中必须包含的Tag
  - 基于Quoto的外汇订单可能会要求必须包含QuoteID(117)
  - D订单可能要求必须包含Account(1) tag

- 对于Quote必须回复Ack(Hardcode了QuoteResponseLevel <301>)
  - Quote Acknowledgement (b) message. It is intended to provide application level acknowledgement of quotes. 

## User Defined Fields: 用户自定义域

为给用户提供最大的灵活性，FIX协议允许用户自定义域。 这些域在认同的参与者之间实现、应用，并且应注意避免冲突。
Tag数在5000 到9999保留用于用户自定义域。这些tag值用于企业联盟的信息交换。可以通过FIX网站进行注册。
10000以上保留用于单一企业内部使用。不用注册。

- MsgType <35> field   Type: String

Defines message type. ALWAYS THIRD FIELD IN MESSAGE. (Always unencrypted)
Note: A "U" as the first character in the MsgType <35> field (i.e. U1, U2, etc) indicates that the message format is privately defined between the sender and receiver.

## Which tag is used in FIX Protocol to denote an order is for equity or for future options?
FIX tag 167 (SecurityType) should be used to identity asset type. In FIX 4.4, you are recommended to use CFICode (461).

## FIX数据包的大小

### Base Network

- Size of Ethernet frame - 24 Bytes
- Size of IPv4 Header (without any options) - 20 bytes
- Size of TCP Header (without any options) - 20 Bytes

Total size of an Ethernet Frame carrying an IP Packet with an empty TCP Segment - 24 + 20 + 20 = 64 bytes

### Body Length

- Logon (10 tags) - 80 bytes
- Single Order (16 tags) - 150 bytes
- Execution Report (28 tags) - 250 bytes
- Quote (Single Side, 22 tags) - 250 bytes
- Quote (Combined, 30 tags) - 350 bytes
