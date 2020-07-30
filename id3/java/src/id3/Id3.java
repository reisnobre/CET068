package id3;

import trainningSet.TrainningSet;

public class Id3 {
	
	Node root;
	TrainningSet set;
	
	/**
	 * This class performs the Id3 mining proccess
	 */
	public Node mine(Node n, TrainningSet set) {
		if (set.hasOnlyOneValue()) {
			return set.getMoreFrequentValue(); 
		}
		Node root = set.getBestEntropy();
		for (Node b: root.getBranches()) {
			mine(b, set.subSet(b));
		}
		return root;
	}

}
