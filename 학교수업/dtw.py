{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from scipy.spatial.distance import euclidean\n",
    "from fastdtw import fastdtw\n",
    "\n",
    "# 난수 생성기 시드 설정\n",
    "np.random.seed(0)\n",
    "\n",
    "time_series_data = []\n",
    "# 1. 다섯 개의 서로 다른 길이를 가진 시계열 데이터를 무작위로 생성\n",
    "for i in range(5):\n",
    "    length = np.random.randint(50, 200)  # 50과 200 사이의 임의의 길이 선택\n",
    "    time_series_data.append(np.random.rand(length))  # 해당 길이만큼 무작위 데이터 생성\n",
    "\n",
    "# 2. 중간 크기의 시계열 데이터를 기준으로 다른 데이터와의 DTW를 계산\n",
    "reference = time_series_data[2]  # 세 번째 시계열 데이터를 기준 데이터로 설정\n",
    "dtw_distances = []\n",
    "\n",
    "# print(reference)\n",
    "\n",
    "for series in time_series_data:\n",
    "    print(series)\n",
    "    # distance, path = fastdtw(reference, series, dist=euclidean)  # 기준 데이터와 다른 시계열 데이터 간의 DTW 계산\n",
    "    # dtw_distances.append(distance)  # 계산된 DTW를 리스트에 추가\n",
    "\n",
    "# # DTW의 평균 및 분산을 계산하여 학습 결과 데이터 생성\n",
    "# average_dtw_distance = np.mean(dtw_distances)\n",
    "# variance_dtw_distance = np.var(dtw_distances)\n",
    "\n",
    "# learning_result = {'average': average_dtw_distance, 'variance': variance_dtw_distance}\n",
    "\n",
    "# # 3. 무작위 인식 시계열 데이터를 입력하여 학습 결과와의 대응 관계 및 유사도 계산\n",
    "# random_recognition_series = np.random.rand(100)  # 1차원 무작위 인식 시계열 데이터 생성\n",
    "\n",
    "# distance, path = fastdtw(random_recognition_series, reference, dist=euclidean)  # 인식 데이터와 기준 데이터 간의 DTW 계산\n",
    "\n",
    "# # 거리를 평균 DTW 거리로 나눈 후 음수를 취해 유사도 점수 계산 (유사도 점수는 0~1 사이의 값)\n",
    "# similarity_score = np.exp(-distance / average_dtw_distance)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
