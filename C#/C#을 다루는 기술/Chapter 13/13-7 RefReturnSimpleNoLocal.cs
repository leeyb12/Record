// 참조 반환을 통해 반환된 결과에 증가 연산을 바로 사용

static void Main()
{
    int x = 10;
    RefReturn(ref x)++;  // 반환된 변수의 값을 바로 증가시킴
    Console.WriteLine(x);
}

static ref int RefReturn(ref int p)
{
    return ref p;
}