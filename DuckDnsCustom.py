import requests
import ifcfg
from os import system
from time import sleep
from socket import gethostbyname
import json

try:
	with open("duckconf.json", 'r+') as file_j:
 		dump = file_j.read()
 		data_ = json.loads(dump)
except Exception as error_r:
	print('Erro ao ler o arquivo conf*.json ->', error_r)



tcp_host_map, port_map = data_['host'], data_['port_map']
domain_duck = data_['domain']
TOKEN = data_['token']


tcp_host_Public = gethostbyname(tcp_host_map)

print("Execute a vpn: sudo openvpn --config calango.first.ovpn")

def ip_get():
	if_c = ifcfg.interfaces()
	if_ip_tun = str(if_c['tun0']['inet'][0])
	return if_ip_tun

def duck_():
	LINK = "https://www.duckdns.org/update?domains={}&token={}&ip={}".format(DOMAIN, TOKEN, tcp_port_Public)
	get = requests.get(LINK)
	if not get.text != "OK":
		print("OK > DuckDNS => Connect..")
		print("Dominio a conectar: {}{}:{}".format(DOMAIN, domain_duck, port_map))
		print("IP > metasploit: ", ip_get())
		print("Public ip >", tcp_host_Public)
	else:
		print("Falha ==> indentifique a configuração ")


while True:
	duck_()
	sleep(60)