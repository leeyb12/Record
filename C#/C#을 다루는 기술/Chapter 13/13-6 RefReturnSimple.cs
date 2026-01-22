// 매우 단순한 참조 반환의 예

static void Main()
{
    int x = 10;
    ref int y = ref RefReturn(ref x);
    y++;
    Console.WriteLine(x);
}

static ref int RefReturn(ref int p)
{
    return ref p;
}