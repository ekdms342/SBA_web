import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

class Dataset_csv : 
    # 클래스 생성자 
    # - anscom 데이터 셋 로드 
    def __init__(self) :
        # 클래스가 생성될 때 엠스콤 데이터 셋 로드해 놓기
        # self로 지정된 변수들은 모두 전역변수로 사용가능
        self.df = sns.load_dataset("anscombe")
    
    # 앤스콤 데이터 조회하기 
    def getAnscombeData(self) :
        return self.df
    # HTML 에 넘겨 주기 위한 데이터형태로 조회하기 
    def getAColumn_List(self) :
        
        columns = self.df.columns
        
        df_list = [{columns[0] : d, 
                    columns[1] :x,
                    columns[2] :y} for d,x,y in zip(self.df['dataset'], self.df['x'], self.df['y'])]
        return columns, df_list

    def initVisualization (self) :
        data1 = self.df[(self.df["dataset"] == "I") == True]
        ### dataset 이 II, III, IV에 대해서도 필터링 후 그래프 그려주세요...
        # 변수 : data2, data3, data4를 사용
        data2 = self.df[self.df["dataset"] == "II"]
        data3 = self.df[self.df["dataset"] == "III"]
        data4 = self.df[self.df["dataset"] == "IV"]

        ### 그래프를 그리기 위한 객체 받아 오기
        fig = plt.figure()

        ### 4개 각각의 그래프를 그리기 위한 공간 만들기
        # - subplot 함수 사용
        # - 첫번째 값 : 행을 의미함
        # - 두번째 값 : 열을 의미함
        # - 세번째 값 : 행렬 중 어느 위치에 들어갈지 순서 지정
        # - 2행 2열의 공간을 생성
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3)
        ax4 = fig.add_subplot(2, 2, 4)

        ### subplot에 제목 넣기 : set_title() 함수 사용
        ax1.set_title("data1")
        ax2.set_title("data2")
        ax3.set_title("data3")
        ax4.set_title("data4")

        ### 그래프의 위/아래 사이에 겹쳐서 나오는 부분을 해소하기 위해
        # - 간격 조정을 합니다. tight_layout() 함수 사용
        fig.tight_layout()

        ### 데이터를 넣어서 그림 그리기 : 점으로표시
        ax1.plot(data1["x"], data1["y"], "o", c="red")
        ax2.plot(data2["x"], data2["y"], "o", c="g")
        ax3.plot(data3["x"], data3["y"], "o", c="b")
        ax4.plot(data4["x"], data4["y"], "o", c="y")

        ### 전체 그래프 제목 넣기
        fig.suptitle("Anscombe Data")

        fig.tight_layout()

        ## 우상향 데이터 : 왼쪽 밑에서 오른쪽 위로 분포하는 데이터형태
        ## 우하향 데이터 : 왼쪽 위에서 오른쪽 아래로 분포하는 데이터형태

        plt.savefig("C:/pknu_web/toturial/ml/static/ml/images/anscombe_data.png")
        # C:/pukyung_202301/33Day/images/anscombe_data.png