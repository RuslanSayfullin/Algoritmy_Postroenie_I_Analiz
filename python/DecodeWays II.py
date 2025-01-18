# Input: s = "*"
# Output: 9

def numDecodings(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if s[i - 1] == '*':
            dp[i] += 9 * dp[i - 1]
        elif s[i - 1] != '0':
            dp[i] += dp[i - 1]

        if i > 1:
            if s[i - 2] == '*':
                if s[i - 1] == '*':
                    dp[i] += 15 * dp[i - 2]
                elif '0' <= s[i - 1] <= '6':
                    dp[i] += 2 * dp[i - 2]
                else:
                    dp[i] += dp[i - 2]
            elif s[i - 2] == '1':
                if s[i - 1] == '*':
                    dp[i] += 9 * dp[i - 2]
                else:
                    dp[i] += dp[i - 2]
            elif s[i - 2] == '2':
                if s[i - 1] == '*':
                    dp[i] += 6 * dp[i - 2]
                elif '0' <= s[i - 1] <= '6':
                    dp[i] += dp[i - 2]

        dp[i] %= MOD

    return dp[n]

if __name__ == "__main__":
    result = numDecodings(s = "*")
    print(result)