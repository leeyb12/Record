// 예제 14-2를 로즐린이 변환한 결과

private struct MainLocals  // Main 내부의 지역 변수를 포함하는 변경 가능한 생성
{
    public int i;
}

static void Main()
{
    // 지역 메서드 내에서 사용할 구조체 타입의 변수 생성/사용
    MainLocals locals = new MainLocals();
    locals.i = 0;

    // 추가로 생성한 메서드에 구조체를 참조로 전달
    AddToI(5, ref locals);
    AddToI(10, ref locals);

    Console.WriteLine(locals.i);
}

// 지역 메서드를 이용하여 추가로 생성한 메서드
static void AddToI(int amount, ref MainLocals locals)
{
    locals.i += amount; 
}