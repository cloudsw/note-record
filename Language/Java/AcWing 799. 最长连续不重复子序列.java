package com.wd;


import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw  = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int[] s = new int[100010];
        String[] str = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }

        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            s[arr[i]] ++;
            while (j < i && s[arr[i]] > 1){
                s[arr[j++]] --;
            }
            res = Math.max(res, i -j + 1);
        }
        bw.write(String.valueOf(res));
        bw.flush();
    }
}
// 双指针算法