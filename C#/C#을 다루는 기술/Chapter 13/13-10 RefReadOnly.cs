// 읽기 전용 참조 반환과 읽기 전용 참조 지역 변수

static readonly int field = DateTime.UtcNow.Second;  // 읽기 전용 field 변수를 임의의 값으로 초기화

static ref readonly int GetFieldAlias() => ref field;  // field의 읽기 전용 별칭을 반환

static void Main()
{
    ref readonly int local = ref GetFieldAlias();  // 메서드를 호출하여 읽기 전용 참조 지역 변수를 초기화
    Console.WriteLine(local);
}