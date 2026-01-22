// 패턴과 재귀를 이용하여 피보나치 수열 구현

static int Fib(int n)
{
    switch (n)
    {
        // 상수 패턴을 이용하여 기본 정의를 구현
        case 0: return 0;
        case 1: return 1;

        case var _ when n > 1: return Fib(n - 2) + Fib(n - 1);  // var 패턴과 가드 절을 이용하여 재귀 부분을 구현

        // 패턴 매칭이 이루어지지 않았다면 입력값이 유효하지 않은 것임
        default: throw new ArgumentOutOfRangeException(
            nameof(n), "Input must be non-negative");
    }
}