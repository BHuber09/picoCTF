# Cryptography doesn't have to be complicated, have you ever heard of something called rot13? cvpbPGS{guvf_vf_pelcgb!}

en = "cvpbPGS{guvf_vf_pelcgb!}"

import string

rot13 = string.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
						 "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")

print string.translate(en, rot13)