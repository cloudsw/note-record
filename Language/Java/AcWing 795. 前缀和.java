import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] str = br.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        int[] arr = new int[n];
        int[] sum = new int[n + 1]; //用来存储和数组，new的新数组大小必须比用到的数组大一列，因为sum是从索引1开始的，并且sun[0] = 0。前零个数的和为零
        String[] temp = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(temp[i]);
        }
        for (int i = 1; i <= n; i++) {
            sum[i] = sum[i - 1] + arr[i - 1]; //此时的arr数组需要建议，因为i从1开始。
        }
        while (m-- > 0){
            String[] strs = br.readLine().split(" ");
            int nn = Integer.parseInt(strs[0]);
            int mm = Integer.parseInt(strs[1]);
            System.out.println(sum[mm] - sum[nn - 1]);  //此题目中sout输出较快
//            bw.write(sum[mm] - sum[nn - 1] + "\n"); //bw.write()适合大数据时  "\n"是转义，代表回车
//            bw.flush();
        }

    }
//一维前缀和


}