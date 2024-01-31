class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] answers = new int[temperatures.length];
        for(int i = 0;i <temperatures.length ; i++)
        {
            int count = 0;
            for(int j=i+1;j<temperatures.length  ; j++)
            {
                if(temperatures[i] < temperatures[j])
                {
                    count = j - i;
                    break; 
                }
            }
            answers[i] = count;

        }
        return answers;
    }
        
}
