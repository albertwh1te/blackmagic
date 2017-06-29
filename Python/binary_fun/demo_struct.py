# -*- coding: utf-8 -*-
import struct
def demo1():
    # ä½¿ç”¨bin_buf = struct.pack(fmt, buf)å°†bufÃ¤¸ººŒ¿›ˆ¶•°»„bin_buf
    # ä½¿ç”¨buf = struct.unpack(fmt, bin_buf)å°†bin_bufÃ¤ºŒ¿›ˆ¶•°»„½¬¢›buf

    # æ•´å‹æ•° -> äºŒè¿›åˆ¶æµ
    buf1 = 256
    bin_buf1 = struct.pack('i', buf1) # 'i'ä»£è¡¨'integer'
    ret1 = struct.unpack('i', bin_buf1)
    print bin_buf1, '  <====>  ', ret1

    # æµ®ç‚¹æ•° -> äºŒè¿›åˆ¶æµ
    buf2 = 3.1415
    bin_buf2 = struct.pack('d', buf2) # 'd'ä»£è¡¨'double'
    ret2 = struct.unpack('d', bin_buf2)
    print bin_buf2, '  <====>  ', ret2

    # å­—ç¬¦ä¸² -> äºŒè¿›åˆ¶æµ
    # buf3 = 'Hello World'
    buf3 = 'Hello World1'
    bin_buf3 = struct.pack('11s', buf3) # '11s'ä»£è¡¨é•¿åº¦ä¸º11çš„'string'å­—ç¬¦æ•°ç»„
    ret3 = struct.unpack('11s', bin_buf3)
    print bin_buf3, '  <====>  ', ret3

    # ç»“æ„ä½“ -> äºŒè¿›åˆ¶æµ
    # å‡è®¾æœ‰ä¸€ä¸ªç»“æ„ä½“
    # struct header {
    #   int buf1;
    #   double buf2;
    #   char buf3[11];
    # }
    bin_buf_all = struct.pack('id11s', buf1, buf2, buf3)
    ret_all = struct.unpack('id11s', bin_buf_all)
    print bin_buf_all, '  <====>  ', ret_all

demo1()
