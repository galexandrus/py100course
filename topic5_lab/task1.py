import pprint

dec_bin_oct_hex = [{"dec": n, "bin": bin(n), "oct": oct(n), "hex": hex(n)} for n in range(16)]

pp = pprint.PrettyPrinter()
pp.pprint(dec_bin_oct_hex)
