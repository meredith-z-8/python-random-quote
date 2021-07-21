import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)-1
  rnd = random.randint(0,last)
  rnd2 = random.randint(0,last)
  print(quotes[rnd][:len(quotes[rnd])-1], quotes[rnd2][:len(quotes[rnd2])-1], sep = ' and ')
  

if __name__== "__main__":
  primary()
