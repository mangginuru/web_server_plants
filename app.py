from flask import Flask
from flask import request, jsonify, redirect
import json
from plants_API.plants_prediction.inference import get_prediction
from plants_API.naver_shop_api.searchAPI import naver_searchAPI


app = Flask(__name__)

black_list = []
white_list = []


## 식물 인식 사진을 요청 받으면 인식 후 
## 식물 이름(국문)을 반환한다.
#HTML 렌더링
@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files.get('file')
		if not file:
			return "파일 이름이 없습니다..."
		img_bytes = file.read()
		class_kr= get_prediction(image_bytes=img_bytes)
		predict_results = {
			"kr_name": class_kr
		}
		return jsonify(predict_results)	

## 네이버 쇼핑 식물 검색
## ex) '아레카야자'라고 검색할시 식물 구매 리스트가 15개를 반환한다.
@app.route('/product', methods=['GET', 'POST'])
def product():
	if request.method == 'POST':
		if False == request.is_json:
			return redirect(request.url)
		text = request.get_json()
		text = text["data"]
		if not text:
			return "검색 결과가 없습니다."
		if text == "시서스":
			product_sysus = naver_searchAPI("시서스 식물")
			return product_sysus
		product_result = naver_searchAPI(text)
		return product_result	

#서버 실행
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=0000, debug = True)