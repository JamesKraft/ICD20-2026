out = input("Enter:")
word = input("Enter:")
def make_out_word(out, word):
  out1 = (out[0:2])
  out2 = (out[2:4])
  return out1 + word + out2

print(make_out_word(out, word))