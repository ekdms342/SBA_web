import numpy as np
### Tokenizer : 문장에서 단어 분류하기
from keras.preprocessing.text import Tokenizer
### pad_sequences : 정규화(문장 길이 자르기)
from keras.preprocessing.sequence import pad_sequences
### to_categorical : 원-핫 인코딩
# from keras.utils import to_categorical
import keras

class RNN :
    
    def __init__(self) :
        # 클래스가 생성될 때 엠스콤 데이터 셋 로드해 놓기
        # self로 지정된 변수들은 모두 전역변수로 사용가능
        self.model = keras.models.load_model("C:/pknu_web/toturial/ml/rnn/model/django_rnn_model.h5")
        text = """경마장에 있는 말이 뛰고 있다\n 
        다그의 말이 법이\n
        가는 말이 고와야 오는 말이 곱다\n"""
        
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts([text])
   
    def getModel(self) :
        return self.model
    
    def sentence_generation(self,current_word,n):
        init_word = current_word
        sentence = ""
        
        ### 전달 받은 값 n번 반복시키기
        for _ in range(n) :
            ### 현재 입력 받은 단어에 대한 정수 인코딩
            encoded = self.tokenizer.texts_to_sequences([current_word])[0]
            ### 단어 자르기 : x값은 5개
            encoded = pad_sequences([encoded], maxlen=5, padding="pre")
            
            ### 예측하기
            result = self.model.predict(encoded, verbose=0)
            ### 예측결과 중에 가장 빈self.model도가 큰값 결정하기
            result = np.argmax(result, axis=1)
            print("result = ", result)
            
            for word, index in self.tokenizer.word_index.items():
                ## 만약 예측한 단어와 인덱스와 동일한 단어가 있다면 break
                if index == result :
                    break
            
            ### 현재 입력된 단어와 예측 단어 조합하기
            current_word = current_word + " " + word
            
            ### 예측 단어 조합을 변수에 저장
            sentence = sentence + " " + word
            
        ### 함수가 전달받은 단어에 대한 조합할 단어(문장) 합치기    
        sentence = init_word + sentence
        
        return sentence
