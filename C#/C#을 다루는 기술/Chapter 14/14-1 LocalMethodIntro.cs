// 지역 변수를 사용하는 간단한 지역 메서드

static void Main()
{
    int x = 10;  // 메서드 내부에서 사용할 지역 변수 선언

    // 지역 메서드를 두 번 호출
    PrintAndIncrementX();
    PrintAndIncrementX();

    Console.WriteLine($"After calls, x = {x}");

    // 지역 메서드
    void PrintAndIncrementX()
    {
        Console.WriteLine($"x = {x}");
        x++;
    }
}