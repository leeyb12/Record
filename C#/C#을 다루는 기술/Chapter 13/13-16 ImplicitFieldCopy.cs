// 읽기 전용 필드와 읽고 쓸 수 있는 필드를 통해 각 구조체의 속성에 접근

class ImplictFieldCopy
{
    private readonly YearMonthDay readOnlyField = 
        new YearMonthDay(2018, 3, 1);
    private YearMonthDay readWriteField = 
        new YearMonthDay(2018, 3, 1);
    
    public void CheckYear()
    {
        int readOnlyFieldYear = readOnlyField.Year;
        int readWriteFieldYear = readWriteField.Year;
    }
}