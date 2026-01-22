// stackalloc과 Span<char>를 이용해서 랜덤 문자열 생성

static string Generate(string alphabet, Random random, int length)
{
    Span<char> chars = stackalloc char[length];
    for (int i = 0; i < length; i++)
    {
        chars[i] = alphabet[random.Next(alphabet.Length)];
    }
    return new string(chars);
}