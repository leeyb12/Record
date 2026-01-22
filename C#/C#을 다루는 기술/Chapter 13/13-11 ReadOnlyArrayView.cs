// 배열에 대해 그 내용을 복사하지 않고 읽기 전용으로만 접근할 수 있는 뷰 생성

class ReadOnlyArrayView<T>
{
    private readonly T[] values;

    // 내용을 복사하지 않고 배열에 대한 참조만 복사
    public ReadOnlyArrayView(T[] values) =>
        this.values = values;
    
    // 배열 내의 개별 요소에 대한 읽기 전용 별칭을 반환
    public ref readonly T this[int index] =>
        ref values[index];
}
...

static void Main()
{
    var array = new int[] { 10, 20, 30 };
    var view = new ReadOnlyArrayView<int>(array);

    ref readonly int element = ref view[0];

    // 배열의 내용을 수정하면 참조 지역 변수에도 그대로 반영
    Console.WriteLine(element);
    array[0] = 100;
    Console.WriteLine(element);
}