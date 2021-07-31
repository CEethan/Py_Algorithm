#sorted()
result = sorted([3, 2, 9, 6, 1])
#오름차순
reverse_result = sorted([3, 2, 9, 6, 1], reverse=True)
#내림차순
print(result)
print(reverse_result)


#stored() 키속성
array = [('이창민', 34), ('이순신', 12), ('홍길동', 27)]
array_result = sorted(array, key=lambda x: x[1], reverse=True)
print(array_result)
#key의 값에 따라 수가 큰 순서대로 정렬