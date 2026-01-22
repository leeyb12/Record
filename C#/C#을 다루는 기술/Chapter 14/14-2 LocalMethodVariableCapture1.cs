// 지역 변수의 값을 수정하는 지역 메서드

static void Main()
{
    int i = 0;
    AddToI(5);
    AddToI(10);
    Console.WriteLine(i);
    void AddToI(int amount) => i += amount;
}