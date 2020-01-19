package trainningSet;

import java.util.ArrayList;

import id3.Node;

public class TrainningSet {
	
	private ArrayList<MiningAttribute> attrList;
	private MiningAttribute classAttr;

	/**
	 * This method returns true if the training set has
	 * only one class value
	 * @return
	 */
	public boolean hasOnlyOneValue() {
		return classAttr.hasOnlyOneValue();
	}

	/**
	 * This method returns a leaf node with the more frequent
	 * class value found in the trainning set
	 * @return
	 */
	public Node getMoreFrequentValue() {
		// TODO Auto-generated method stub
		return null;
	}

	/**
	 * This method returns a node with the best entropy between all 
	 * attributes in this trainning set
	 * @return
	 */
	public Node getBestEntropy() {
		// TODO Auto-generated method stub
		return null;
	}

	/**
	 * This method generates and returns a new trainning set
	 * being a subset of this.
	 * It selects only the value set in the node b and
	 * does not contains the attribute b
	 * @param b
	 * @return
	 */
	public TrainningSet subSet(Node b) {
		// TODO Auto-generated method stub
		return null;
	}

}
