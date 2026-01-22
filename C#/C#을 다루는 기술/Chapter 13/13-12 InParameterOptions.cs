// in 매개변수에 대해 인수를 전달할 때 유효한 경우와 유효하지 않은 경우

static void PrintDateTime(in DateTime value)  // in 매개변수를 취하는 메서드 정의
{
    string text = value.ToString(
        "yyyy-MM-dd'T'HH:mm:ss",
        CultureInfo.InvariantCulture);
    Console.WriteLine(text);
}

static void Main()
{
    DateTime start = DateTime.UtcNow;
    PrintDateTime(start);  // 암시적으로 변수의 참조를 전달
    PrintDateTime(in start);  // 명시적으로 변수의 참조를 전달(in 한정자가 사용되었으므로)
    PrintDateTime(start.AddMinutes(1));  // 보이지 않는 지역 변수 복사본을 생성한 후 이에 대한 참조를 전달
    PrintDateTime(in start.AddMinutes(1));  // 컴파일 시 오류: 인수를 참조로 전달할 수 없음
}