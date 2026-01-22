// 참조 지역 변수를 이용하여 특정 객체의 인스턴스 필드에 별칭 부여

class RefLocalField
{
    private int value;

    static void Main()
    {
        var obj = new RefLocalField();  // RefLocalField의 인스턴스 생성
        ref int tmp = ref obj.value;  // 첫 번째 인스턴스의 필드를 참조하는 참조 지역 변수 선언
        tmp = 10;  // 참조 지역 변수에 새로운 값을 할당
        Console.WriteLine(obj.value);  // 인스턴스 필드의 값이 변경되었는지 확인

        obj = new RefLocalField();  // 새롭게 RefLocalField 인스턴스를 생성한 후 obj 변수에 재할당
        Console.WriteLine(tmp);  // tmp가 여전히 첫 번째 인스턴스의 필드를 참조하고 있음을 확인
        Console.WriteLine(obj.value);  // 두 번째 인스턴스의 필드 값이 실제로 0임을 확인
    }
}