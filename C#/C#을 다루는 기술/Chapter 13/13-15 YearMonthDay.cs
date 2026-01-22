// 간단한 year/month/day 구조체

public struct YearMonthDay
{
    public int Year { get; }
    public int Month { get; }
    public int Day { get; }

    public YearMonthDay(int year, int month, int day) =>
        (Year, Month, Day) = (year, month, day);
}