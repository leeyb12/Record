// 여러 범위에서 각기 선언된 변수를 캡처

static void Main()
{
    DateTime now = DateTime.UtcNow;
    int hour = now.Hour;
    if (hour > 5)
    {
        int minute = now.Minute;
        PrintValues();

        void PrintValues() => 
            Console.WriteLine($"hour = {hour}; minute = {minute}");
    }
}