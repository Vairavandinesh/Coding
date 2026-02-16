import java.util.*;
public class bubble_sort{
    public static void main(String[] args){
        int [] arr={7,2,9,6,4};
        for(int i=0;i<arr.length-1;i=i+1){
            for(int j=0;j<arr.length-i-1;j=j+1){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}