package com.wd;


import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw  = new BufferedWriter(new OutputStreamWriter(System.out));

        //n是字符串p的大小
        int n = Integer.parseInt(br.readLine());
        String temp = br.readLine();
        char[] p = new char[n + 1];
        for (int i = 0; i < n; i++) {
            p[i + 1] = temp.charAt(i);
        }
        //m是字符串s的大小
        int m = Integer.parseInt(br.readLine());
        String tems = br.readLine();
        char[] s = new char[m + 1];
        for (int i = 0; i < m; i++) {
            s[i + 1] = tems.charAt(i);
        }

        int[] next = new int[n + 1];

        //求next数组
        for (int i = 2, j = 0; i <= n; i++) {
            while (j != 0 && p[i] != p[j + 1])
                j = next[j];
            if (p[i] == p[j + 1])
                j++;
            next[i] = j;
        }
        //kmp匹配
        for (int i = 1, j = 0; i <= m; i++) {
            while (j != 0 && s[i] != p[j + 1])
                j = next[j];
            if (s[i] == p[j + 1])
                j++;
            if (j == n){
                bw.write((i - n) + " ");
                // bw.flush();  此处flush会TLE。等数据全部缓存结束后，再flush就不会TLE
                j = next[j];
            }
        }
        bw.flush();
    }
}

