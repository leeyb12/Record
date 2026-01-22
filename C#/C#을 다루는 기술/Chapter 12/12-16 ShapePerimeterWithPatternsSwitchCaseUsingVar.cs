// 변수에 문제가 있을 때 var 패턴을 이용하여 대응

static double Perimeter(Shape shape)
{
    switch (shape ?? CreateRandomShape())
    {
        case Rectangle rect:
            return 2 * (rect.Height + rect.Width);
        case Circle circle:
            return 2 * PI * circle.Radius;
        case Triangle triangle:
            return triangle.SideA + triangle.SideB + triangle.SideC;
        case var actualShape:
            throw new InvaliOperationException(
                $"Shape type {actualShape.GetType()} perimeter unknown");
    }
}