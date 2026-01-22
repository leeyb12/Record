// 타입 패턴을 이용하는 제네릭 메서드

static void DisplayShapes<T>(List<T> shapes) where T : shape
{
    foreach (T shape in shapes)  // 변수의 타입은 타입 매개변수(T)
    {
        switch (shape)  // 이 변수에 대해 switch 문 구성
        {
            case Circle c:  // 구체적인 타입으로 변환하기 위해서 타입 변환 시도
                Console.WriteLine($"Circle radius {c.Radius}");
                break;
            case Rectangle r:
                Console.WriteLine($"Rectangle {r.Width} x {r.Height}");
                break;
            case Triangle t:
                Console.WriteLine(
                    $"Triangle sides {t.SideA}, {t.SideB}, {t.SideC}");
                break;
        }
    }
}