# 문자열 함수

## startswith()
```python
word = "superman"
print(word.startswith('s'))  # True

if word.startswith('a'):
    print("a로 시작하는 단어입니다.")
```

```python
# 트럼프 대통령 트윗을 공백 기준으로 분리한 리스트입니다. 수정하지 마세요.
trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for', 'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']

def print_korea(tweet):
    '''
    문자열로 구성된 리스트에서 k로 시작하는 문자열을 출력합니다.
    '''
    for i in tweet:
        if i.startswith('k') == True:
            print(i)
      
print_korea(trump_tweets)
```

## split()
```python
intro = "제 이름은 엘리스입니다."
print(intro.split())
# ["제", "이름은", "엘리스입니다"]

fruits = "사과,귤,배,바나나"
print(fruits.split(','))
# ["사과", "귤", "배", "바나나"]
```

```python
# 트럼프 대통령의 트윗으로 구성된 문자열입니다.
trump_tweets = "thank you to president moon of south korea for the beautiful welcoming ceremony it will always be remembered"

def break_into_words(text):
    words = list(text.split(' '))
    
    return words

print(break_into_words(trump_tweets))
```

## lower(), upper()
```python
intro = "My name is Elice!"
print(intro.lower())
# "my name is elice!"
print(intro.upper())
# "MY NAME IS ELICE!"
```

