// char[]를 사용하여 랜덤 문자열 생성

static string Generate(string alphabet, Random random, int length)
{
    char[] chars = new char[length];
    for (int i = 0; i < length; i++)
    {
        chars[i] = alphabet[random.Next(alphabet.Length)];
    }
    return new string(chars);
}