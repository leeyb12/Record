// 여러 개의 참조 매개변수에 동일한 변수를 사용

static void Main()
{
    int x = 5;
    IncrementAndDouble(ref x, ref x);
    Console.WriteLine(x);
}

static void IncrementAndDouble(ref int p1, ref int p2)
{
    p1++;
    p2 += 2;
}