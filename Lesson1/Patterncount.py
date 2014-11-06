import operator

def PatternToNumber(Pattern):
  value = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
  Number = 0
  for i in range(len(Pattern)):
    #print('Value:',value[Pattern[-(i+1)]]*4**(i),i)
    Number += value[Pattern[-(i+1)]]*4**(i)
  return Number

def NumberToPattern(Number, Length):
  value = {0 : 'A', 1: 'C', 2 : 'G', 3 : 'T'}
  Pattern = ''
  for i in list(range(Length))[::-1]:
    Cociente = Number//(4**(i))
    Resto = Number % (4**(i))
    Pattern += value[Cociente]
    Number = Resto
  return Pattern

def patterncount(Text, Pattern):
  count = 0
  for i in range(len(Text)-len(Pattern)+1):
    if Text[i:i+len(Pattern)] == Pattern:
      count += 1
  return count

def frequentwords(Text, k):
  kmers = {}
  for i in range(len(Text)-k+1):
    kmer = Text[i:i+k]
    if kmers.get(kmer,''):
      kmers[kmer] += 1
    else:
      kmers[kmer] = 1
  topk = 0
  for key in kmers.keys():
    if kmers[key] > topk:
      topk = kmers[key]
      topkmers = [key]
    elif kmers[key] == topk:
      topkmers.append(key)
  return (topkmers, topk)

def ComputingFrequencies(Text, k):
  FrequencyArray = [0]*4**k
  for i in range(len(Text)-k+1):
    Pattern = Text[i:i+k]
    j = PatternToNumber(Pattern)
    FrequencyArray[j] += 1
  return FrequencyArray

def FasterFrequentWords(Text,k):
  FrequentPatterns = []
  FrequencyArray = ComputingFrequencies(Text,k)
  maxCount = max(FrequencyArray)
  for i in range(len(FrequencyArray)):
    if FrequencyArray[i] == maxCount:
      Pattern = NumberToPattern(i,k)
      FrequentPatterns.append(Pattern)
  return FrequentPatterns, maxCount


for n in FasterFrequentWords("TGCTGAGTAGTTATGAATGCTGTCTAATGCTAGTTCGGGTCCGCAGTATATCGGTGAGGCAAACAGGAGCTTATTACCATAAGGATACGGAGGGCATATGAGAACGCAGGTGTAGCGTGAGTCGCAGCCGGCCATGGAGACTTTATTAGCCCGCCTCGAAGATATCACTGATGAGTCAGCATCCTAGCCAACTTTCTTGGCATAGTTGCACCTCATCCGTGAGGAATTTCATGGAAACCTGACACAACCGTTATTTGGCAGGCATCCATGAACTGTATTAAGCGGTGACACTGTTTGTCCTGCCCCCGGGACATAGAGGAAGACCCTCACTGAGATATTTCTGATGTTCGACGCTAAACTAAAATACTATGGTGTGTCCTGTGTTCTATGCGTTGCCCGCTGTTCTGCGCACAACATACATTCAGCGGTATCTCCGGAAATAGCACCTCTTATAGAATCGATCGCTGTATGACACATTGGCGCGCGCTGTTTGGAATAGTCATATACTACGTGCTTGGTGGTGCGGACTTGGAATAATGCTTGGTCAGACCGTACATCTGCAGGAGGGACATACCACCATAGTAACGCTAATTCCACATGTGTCTGCGTTTGAAGCCGAGAGCGCAAGGAA",8):
  print(n,end = " ")