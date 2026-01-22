// 시퀀스에서 홀수와 짝수를 셈

static (int even, int odd) CountEvenAndOdd(IEnumerable<int> values)
{
    var result = (even: 0, odd: 0);
    foreach (var value in values)
    {
        // 증가시켜야 할 변수를 선택
        ref int counter = ref (value & 1)  == 0 ?
            ref result.even : ref.result.odd;
        
        counter++;  // 값을 1 증가시킴
    }
    return result;
}