from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
  my_dict={}
  for i in range(0, len(word)):
    my_dict[word[i]]=i

  for key in my_dict:
    counter=0
    for letters in word:
      if letters == key:
        counter+=1
        my_dict[key]=counter
  return my_dict
    





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
