package com.wd;


import java.io.*;

public class Main {
    static int N = 100010, idx;
    static int[][] son  = new int[N][26];
    static int[] cnt = new int[N];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            String[] str = br.readLine().split(" ");
            if ("I".equals(str[0]))  //字符串比较用equals， ==比较内存地址
                insert(str[1]);
            else
                bw.write(query(str[1]) + "\n");
        }
        bw.flush();
    }

    public static void insert(String str){
        int p = 0;
        for (int i = 0; i < str.length(); i++) {
            int u = str.charAt(i) - 'a';
            if (son[p][u] == 0)
                son[p][u] = ++ idx;  //如果当前这个点上不存在对应的字母的话，创建出来
            p = son[p][u];
        }
        cnt[p] ++;  //p对应的点就是最后一个点，cnt[p]++表示以这个点结尾的单词数量加1
    }

    public static int query(String str){
        int p = 0;
        for (int i = 0; i < str.length(); i++) {
            int u = str.charAt(i) - 'a';  //a~z  映射成0~25
            if (son[p][u] == 0)
                return 0;
            p = son[p][u];
        }
        return cnt[p];  //返回以p结尾的单词数量
    }
}

