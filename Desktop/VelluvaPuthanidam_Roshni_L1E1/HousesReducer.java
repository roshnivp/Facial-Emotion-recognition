package Houses;

/**
 * Created by Roshni Velluva Puthanidam on 20/09/16.
 */
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import java.io.IOException;
import java.text.DecimalFormat;


public class HousesReducer  extends Reducer <Text,IntWritable,Text,FloatWritable> {
   // private IntWritable result = new IntWritable();
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

        // TODO: initialize min and max values
             long tempMin = 0, tempMax = 0, min = Long.MAX_VALUE , max = Long.MIN_VALUE;

             float sum = 0;
             int count = 0;
        // TODO: loop through values to determine min, max, count, and sum
           for(IntWritable val : values){
               sum+= val.get();
               count+= 1;
               tempMin= new Long(String.valueOf(val)).longValue();
               tempMax= new Long(String.valueOf(val)).longValue();
               if(tempMin < min) {
                   min= tempMin;
               }
               if(tempMax > max) {
                   max= tempMax;
               }
           }


        // TODO: calculate mean
        float mean = sum/count;
        // TODO: write (key, min) to context
        context.write(new Text(key),new FloatWritable(min));
        // TODO: write (key, mean) to context
        context.write(new Text(key),new FloatWritable(mean));
        // TODO: write (key, max) to context
        context.write(new Text(key),new FloatWritable(max));
    }
}