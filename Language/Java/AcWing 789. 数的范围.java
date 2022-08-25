import java.io.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine()); //将字符串转换成整数 Integer.parseInt()
        int[] arr = new int[n];
        String[] str = br.readLine().split(" "); //根据空格分割字符串 split(" ")
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }

        ArrayList<Integer> res = bserarch(arr, 0, n - 1, 7);
        bw.write("start is :" + res.get(0) + " " + "end is : " + res.get(1));
        bw.flush();
    }

    public static boolean check(int[] arr, int mid, int num){ //做判断
        return arr[mid] >= num;
    }

    public static ArrayList<Integer> bserarch(int[] arr, int l, int r, int num){
        ArrayList<Integer> list = new ArrayList<>();
        while (l < r){
            int mid = l + r >> 1;
            if (check(arr, mid, num))
                r = mid;
            else
                l = mid + 1;
        }
        int end = l;
        if (arr[l] == num){
            while(arr[end] == num)
                end++;
            list.add(l);
            list.add(end - 1);
        }
        else{
            list.add(-1);
            list.add(-1);
        }
        return list;
    }
}
// 二分搜索算法，前提是顺序的序列