def addone():
    """함수에서 ㅐ입에 사용되는 변수는 지역 변수"""
    i = 30
    i += 1
    print("\t지역 변수 i:", i)

i = 20
print("i:", i)
addone()
print("i:", i)