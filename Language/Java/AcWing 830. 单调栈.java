import java.io.*;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw  = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayDeque<Integer> ad = new ArrayDeque<>();

        int m = Integer.parseInt(br.readLine());
        while(m-- > 0){
            int x = Integer.parseInt(br.readLine());
            while (!ad.isEmpty()){
                if (x > ad.peek()){
                    bw.write(ad.peek() + " ");
                    bw.flush();
                    break;
                }else{
                    ad.pop();
                }
            }
            if (ad.isEmpty()){
                bw.write("-1 ");
                bw.flush();
            }
            ad.push(x);
        }
    }
}
