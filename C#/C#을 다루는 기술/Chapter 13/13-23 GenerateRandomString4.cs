// string.Create를 이용해서 랜덤 문자열 생성

static string Generate(string alphabet, Random random, int length) =>
    string.Create(length, (alphabet, random), (span, state) =>
    {
        var alphabet2 = state.alphabet;
        var random2 = state.random;
        for (int i = 0; i < span.Length; i++)
        {
            span[i] = alphabet2[random2.Next(alphabet2.Length)];
        }
    });