#WordCount.py
#Name: Emma Barnes
#Date: 02/26/2026
#Assignment: Word Count

def main():
  #file_name = input("File (.txt) to open: ")
  while True:
    file_name = input("File (.txt) to open: ")
    try:
      with open(file_name, 'r') as file:
        #content = file.read()
        #print(content)
    
      #textFile = open(file_name, 'r')
        lineCount = 0
        wordCount = 0
        letterCount = 0
        for line in file:
          lineCount = lineCount + 1
      
          words = line.split()
          for w in words:
            wordCount = wordCount + 1
      
          letterCount = letterCount + len(line)
    
      print("Lines:", lineCount)
      print("Words:", wordCount)
      print("Characters:", letterCount)
      break

    except FileNotFoundError:
      print("Error: The file could not be found. Please try again.")
    except (KeyboardInterrupt, SystemExit):
      print("Exiting program.")
      break

if __name__ == '__main__':
  main()
