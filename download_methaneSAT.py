import ee

# Earth Engine 초기화
ee.Initialize()

# 예시: MethaneSAT 데이터셋 불러오기 (데이터셋 ID는 실제 MethaneSAT 데이터셋의 ID로 대체 필요)
methane_data = ee.ImageCollection('MethaneSAT/METHANESAT_DATASET_ID') \
                .filterDate('2022-01-01', '2022-12-31') \
                .filterBounds(ee.Geometry.Point([126.9780, 37.5665]))  # 서울 예시

# 첫 번째 이미지 선택 (필요에 따라 평균 등으로 결합 가능)
image = methane_data.first()

# 내보내기 작업 생성
task = ee.batch.Export.image.toDrive(
    image=image,
    description='MethaneSAT_export',
    folder='EarthEngineExports',
    fileNamePrefix='methanesat_data',
    region=ee.Geometry.Rectangle([126.5, 37.4, 127.2, 37.7]).getInfo(),  # 내보내려는 영역 설정
    scale=30,  # 해상도 (단위: 미터)
    maxPixels=1e9
)

# 작업 시작
task.start()
