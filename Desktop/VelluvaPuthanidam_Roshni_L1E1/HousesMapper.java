package Houses;

/**
 * Created by Roshni Velluva Puthanidam on 20/09/16.
 */
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.hadoop.mapreduce.lib.join.Parser;

import java.util.logging.Logger;

import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class HousesMapper  extends Mapper <LongWritable,Text,Text,IntWritable> {
    private static Log log = LogFactory.getLog(HousesMapper.class);
    int indexNeighbour;
    int indexSalePrice;
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {


        // TODO validate number of tokens in iterator
        // TODO if invalid, then write a message to log

            String[] array=value.toString().split(",");

                 if(array==null | array.length==0){
                     log.info("invalid number of tokens");
                 }

        // TODO: skip  very first record (schema line)
        // TODO: create iterator over record assuming comma-separated fields
                if ( value.toString().contains("MSSubClass")/*Some condition satisfying it is header*/)
                   {
                       indexNeighbour = Arrays.asList(array).indexOf("Neighborhood");
                       indexSalePrice = Arrays.asList(array).indexOf("SalePrice");
                       return;
                   }

                else {
                    // TODO get neighborhodd
                    // TODO validate string is not empty or null
                    // TODO if empty or null, then write a message to log
                    String neighbourhood = array[indexNeighbour];
                    if(neighbourhood == null){
                        log.info("string is empty");
                    }

                    // TODO get price
                    // TODO convert price to int
                    int price = Integer.valueOf(array[indexSalePrice]);


                    // TODO validate the price is greater than zero
                    // TODO if price <= 0, then write a message to log
                    if(price <= 0){
                       log.info("price is less than zero");
                    }

                    // TODO emit key-value as (neighborhood, price)

                    context.write(new Text(neighbourhood), new IntWritable(price));
                }






    }

}

