#WordIndex.py
#Name: Emma Barnes
#Date: 02/26/2026
#Assignment: Word Index

def main():
  while True:
    file_name = input("File (.txt) to index: ")
    #textFile = open("fish.txt", 'r')
    try:
      with open(file_name, 'r') as file:
    
        words = {} #create an empty dictionary
        lineNum = 0
        

        for line in file:
          lineNum = lineNum + 1
          wordList = line.replace('—' , ' ').split()
          for w in wordList:
            w = w.lower()
            w = w.replace("," , "")
            w = w.replace("." , "")
            w = w.replace("!" , "")
            #w = w.replace("—" , " ")
            
            if w in words:
              if lineNum not in words[w]:
                words[w].append(lineNum)
            else:
              words[w] = [lineNum]
        
        for word in words:
          print(word, words[word])
      break
    except FileNotFoundError:
      print("Error: The file could not be found. Please try again.")

    except (KeyboardInterrupt, SystemExit):
      print("Exiting program.")
      break

if __name__ == '__main__':
  main()
