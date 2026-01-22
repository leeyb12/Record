// in 매개변수와 값 매개변수 간의 차이

static void InParameter(in int p, Action action)
{
    Console.WriteLine("Start of InParameter method");
    Console.WriteLine($"p = {p}");
    action();
    Console.WriteLine($"p = {p}");
}

static void ValueParameter(int p, Action action)
{
    Console.WriteLine("Start of ValueParameter method");
    Console.WriteLine($"p = {p}");
    action();
    Console.WriteLine($"p = {p}");
}

static void Main()
{
    int x = 10;
    InParameter(x, () => x++);
    ValueParameter(x, () => x++);
}