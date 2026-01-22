// 참조 지역 변수를 이용하여 배열 요소를 수정

// (0, 0), (1, 1) 등과 같이 값을 가진 배열을 초기화
var array = new (int x, int y)[10];

for (int i = 0; i < array.Length; i++)
{
    array[i] = (i, i);
}

// 배열 요소 각각에 대해 x값을 증가시키고, y값을 두 배로 만듦
for (int i = 0; i < array.Length; i++)
{
    ref var element = ref array[i];
    element.x++;
    element.y *= 2;
}