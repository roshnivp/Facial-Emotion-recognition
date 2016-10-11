package Enron;

import org.apache.hadoop.mapreduce.Partitioner;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class EnronPartitioner<K, V> extends Partitioner<K, V> {
	private int m=22;
	private int firstLetterValue=0;

	public int getPartition(K key, V value, int numReduceTasks) {
		// TODO override getPartition(K, V, int) method
		String domain=key.toString();     //value.toString();
		if(numReduceTasks == 0)
			return 0;

		else if(numReduceTasks == 1){
			return 1 % numReduceTasks;
		}
		else if(numReduceTasks == 2){
			if (domain.matches("^[a-m].*$")| domain.matches("^[0-9].*$")){
				return 2 % numReduceTasks;
			}

			else {

				return 1 % numReduceTasks;
			}

	}
         return -1;
	}
}

