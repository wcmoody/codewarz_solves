import sys

if len(sys.argv)!=2:
    exit("error in usage")


with open(sys.argv[1]) as f:
    lines = f.read().split('\n')
    reverse = False
    for line in lines:
        sentence = ""
        words = line.split(' ')
        for word in words:
            length = len(word)
            if length <= 2:
                sentence += word
            elif length % 2 == 0: ##even words greater than length of 2
                middle = length/2
                beg = word[:middle]
                end = word[middle:]
                sentence += beg[::-1] + end[::-1]
            else: ## odd words
                middle = length/2
                beg = word[:middle]
                end = word[middle+1:]
                sentence += beg[::-1] + word[middle] + end[::-1]
            sentence += " "
        print(sentence.strip())
