// 배열 요소를 노출하는 인덱서에서 참조 반환

class ArrayHolder
{
    private readonly int[] array = new int[10];
    public ref int this[int index] => ref array[index];  // 참조로 배열 요소를 반환하는 인덱서
}

static void Main()
{
    ArrayHolder holder = new ArrayHolder();

    // 동일한 배열 요소를 참조하는 두 개의 참조 지역 변수
    ref int x = ref holder[0];
    ref int y = ref holder[0];

    x = 20;  // x를 이용하여 배열 요소의 값을 변경
    Console.WriteLine(y);  // y를 통해 값이 변경되었음을 확인
}